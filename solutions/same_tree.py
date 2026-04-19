"""
Same Tree
Given the roots of two binary trees p and q, write a function to check if they are the same or not.
Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isSameTree(p, q):
    """
    Check if two binary trees are the same.

    Args:
        p: TreeNode, root of first tree
        q: TreeNode, root of second tree

    Returns:
        bool, True if trees are the same, False otherwise
    """
    if not p and not q:
        return True

    if not p or not q:
        return False

    if p.val != q.val:
        return False

    return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)


if __name__ == "__main__":
    # Test case 1: same trees
    p1 = TreeNode(1)
    p1.left = TreeNode(2)
    p1.right = TreeNode(3)

    q1 = TreeNode(1)
    q1.left = TreeNode(2)
    q1.right = TreeNode(3)

    assert isSameTree(p1, q1) == True

    # Test case 2: different trees
    p2 = TreeNode(1)
    p2.left = TreeNode(2)

    q2 = TreeNode(1)
    q2.right = TreeNode(2)

    assert isSameTree(p2, q2) == False
