"""
Validate Binary Search Tree
Given the root of a binary tree, determine if it is a valid binary search tree (BST).
A valid BST is defined as follows:
- The left subtree of a node contains only nodes with keys less than the node's key.
- The right subtree of a node contains only nodes with keys greater than the node's key.
- Both the left and right subtrees must also be binary search trees.
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isValidBST(root):
    """
    Check if a binary tree is a valid BST using bounds recursion.

    Args:
        root: TreeNode, root of the binary tree

    Returns:
        bool, True if valid BST, False otherwise
    """
    def validate(node, lower, upper):
        if not node:
            return True

        if node.val <= lower or node.val >= upper:
            return False

        return (validate(node.left, lower, node.val) and
                validate(node.right, node.val, upper))

    return validate(root, float('-inf'), float('inf'))


if __name__ == "__main__":
    # Test case 1: valid BST
    root1 = TreeNode(2)
    root1.left = TreeNode(1)
    root1.right = TreeNode(3)

    assert isValidBST(root1) == True

    # Test case 2: invalid BST
    root2 = TreeNode(5)
    root2.left = TreeNode(1)
    root2.right = TreeNode(4)
    root2.right.left = TreeNode(3)
    root2.right.right = TreeNode(6)

    assert isValidBST(root2) == False
