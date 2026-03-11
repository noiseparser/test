"""
Symmetric Tree.

Check whether a binary tree is symmetric (mirror image of itself).
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isSymmetric(root):
    """
    Check if a binary tree is symmetric.

    Args:
        root: Root node of the binary tree

    Returns:
        True if the tree is symmetric, False otherwise
    """
    def is_mirror(left, right):
        if not left and not right:
            return True
        if not left or not right:
            return False
        return (left.val == right.val and
                is_mirror(left.left, right.right) and
                is_mirror(left.right, right.left))

    if not root:
        return True
    return is_mirror(root.left, root.right)


if __name__ == "__main__":
    # Test case 1: Symmetric tree
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(2)
    root1.left.left = TreeNode(3)
    root1.left.right = TreeNode(4)
    root1.right.left = TreeNode(4)
    root1.right.right = TreeNode(3)

    assert isSymmetric(root1) == True

    # Test case 2: Non-symmetric tree
    root2 = TreeNode(1)
    root2.left = TreeNode(2)
    root2.right = TreeNode(2)
    root2.left.right = TreeNode(3)
    root2.right.right = TreeNode(3)

    assert isSymmetric(root2) == False
