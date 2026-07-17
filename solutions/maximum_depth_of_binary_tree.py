"""
Maximum Depth of Binary Tree
Given the root of a binary tree, return its maximum depth.
The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def maxDepth(root):
    """
    Returns the maximum depth of a binary tree.

    Args:
        root: TreeNode, the root of the binary tree

    Returns:
        int, the maximum depth
    """
    if not root:
        return 0

    left_depth = maxDepth(root.left)
    right_depth = maxDepth(root.right)

    return 1 + max(left_depth, right_depth)


if __name__ == "__main__":
    # Test case 1: balanced tree
    root1 = TreeNode(3)
    root1.left = TreeNode(9)
    root1.right = TreeNode(20)
    root1.right.left = TreeNode(15)
    root1.right.right = TreeNode(7)
    assert maxDepth(root1) == 3

    # Test case 2: single node
    root2 = TreeNode(1)
    assert maxDepth(root2) == 1
