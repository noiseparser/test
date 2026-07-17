"""
Binary Tree Right Side View
Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.
"""

from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def rightSideView(root):
    """
    Return the right side view of a binary tree using level-order traversal.

    Args:
        root: TreeNode, root of the binary tree

    Returns:
        List[int], values visible from the right side
    """
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        level_size = len(queue)

        for i in range(level_size):
            node = queue.popleft()

            if i == level_size - 1:
                result.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    return result


if __name__ == "__main__":
    # Test case 1: tree with multiple levels
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(3)
    root1.left.right = TreeNode(5)
    root1.right.right = TreeNode(4)

    assert rightSideView(root1) == [1, 3, 4]

    # Test case 2: single node
    root2 = TreeNode(1)
    assert rightSideView(root2) == [1]
