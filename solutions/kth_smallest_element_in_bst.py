"""
Kth Smallest Element in a BST
Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def kthSmallest(root, k):
    """
    Find the kth smallest element in a BST using in-order traversal.

    Args:
        root: TreeNode, root of the BST
        k: int, the kth position (1-indexed)

    Returns:
        int, the kth smallest value
    """
    count = [0]
    result = [None]

    def inorder(node):
        if not node:
            return

        inorder(node.left)

        count[0] += 1
        if count[0] == k:
            result[0] = node.val
            return

        inorder(node.right)

    inorder(root)
    return result[0]


if __name__ == "__main__":
    # Test case 1: k = 1
    root1 = TreeNode(3)
    root1.left = TreeNode(1)
    root1.right = TreeNode(4)
    root1.left.right = TreeNode(2)

    assert kthSmallest(root1, 1) == 1

    # Test case 2: k = 3
    root2 = TreeNode(3)
    root2.left = TreeNode(1)
    root2.right = TreeNode(4)
    root2.left.right = TreeNode(2)

    assert kthSmallest(root2, 3) == 2
