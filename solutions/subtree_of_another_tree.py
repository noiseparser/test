"""
Subtree of Another Tree
Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.
A subtree of a binary tree is a tree that consists of a node in the original tree and all of this node's descendants.
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isSubtree(root, subRoot):
    """
    Check if subRoot is a subtree of root.

    Args:
        root: TreeNode, root of main tree
        subRoot: TreeNode, root of potential subtree

    Returns:
        bool, True if subRoot is a subtree of root
    """
    if not root:
        return False

    if isSameTree(root, subRoot):
        return True

    return isSubtree(root.left, subRoot) or isSubtree(root.right, subRoot)


def isSameTree(p, q):
    """Helper function to check if two trees are identical."""
    if not p and not q:
        return True

    if not p or not q:
        return False

    if p.val != q.val:
        return False

    return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)


if __name__ == "__main__":
    # Test case 1: subRoot is a subtree
    root1 = TreeNode(3)
    root1.left = TreeNode(4)
    root1.right = TreeNode(5)
    root1.left.left = TreeNode(1)
    root1.left.right = TreeNode(2)

    subRoot1 = TreeNode(4)
    subRoot1.left = TreeNode(1)
    subRoot1.right = TreeNode(2)

    assert isSubtree(root1, subRoot1) == True

    # Test case 2: subRoot is not a subtree
    root2 = TreeNode(3)
    root2.left = TreeNode(4)
    root2.right = TreeNode(5)
    root2.left.left = TreeNode(1)
    root2.left.right = TreeNode(2)

    subRoot2 = TreeNode(4)
    subRoot2.left = TreeNode(1)

    assert isSubtree(root2, subRoot2) == False
