"""
Lowest Common Ancestor of a Binary Search Tree
Given a binary search tree (BST) of unique values, and two nodes from the BST, find the lowest common ancestor (LCA) of the two nodes.
The lowest common ancestor between two nodes p and q in a BST is the lowest node in the tree that has both p and q as descendants.
"""


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def lowestCommonAncestor(root, p, q):
    """
    Find the lowest common ancestor of two nodes in a BST.

    Args:
        root: TreeNode, root of the BST
        p: TreeNode, first node
        q: TreeNode, second node

    Returns:
        TreeNode, the lowest common ancestor
    """
    current = root

    while current:
        if p.val < current.val and q.val < current.val:
            current = current.left
        elif p.val > current.val and q.val > current.val:
            current = current.right
        else:
            return current


if __name__ == "__main__":
    # Test case 1: LCA is not one of the nodes
    root1 = TreeNode(6)
    root1.left = TreeNode(2)
    root1.right = TreeNode(8)
    root1.left.left = TreeNode(0)
    root1.left.right = TreeNode(4)
    root1.left.right.left = TreeNode(3)
    root1.left.right.right = TreeNode(5)
    root1.right.left = TreeNode(7)
    root1.right.right = TreeNode(9)

    p1 = root1.left
    q1 = root1.right
    assert lowestCommonAncestor(root1, p1, q1).val == 6

    # Test case 2: LCA is one of the nodes
    p2 = root1.left
    q2 = root1.left.right
    assert lowestCommonAncestor(root1, p2, q2).val == 2
