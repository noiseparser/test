"""
Invert Binary Tree: Given the root of a binary tree, invert the tree (swap the left
and right children at each node), and return the root of the inverted tree.
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def invertTree(root):
    """
    Invert a binary tree by swapping left and right children at each node.

    Args:
        root: Root node of the binary tree

    Returns:
        Root of the inverted tree
    """
    if root is None:
        return None

    # Swap the left and right children
    root.left, root.right = root.right, root.left

    # Recursively invert left and right subtrees
    invertTree(root.left)
    invertTree(root.right)

    return root


def tree_to_list(root):
    """Helper to convert tree to list for testing (level-order traversal)."""
    if not root:
        return []

    result = []
    queue = [root]

    while queue:
        node = queue.pop(0)
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)

    # Remove trailing Nones
    while result and result[-1] is None:
        result.pop()

    return result


if __name__ == "__main__":
    # Test case 1: [2,1,3] -> [2,3,1]
    root1 = TreeNode(2, TreeNode(1), TreeNode(3))
    inverted1 = invertTree(root1)
    assert tree_to_list(inverted1) == [2, 3, 1]

    # Test case 2: empty tree
    assert invertTree(None) is None
