"""
Construct Binary Tree from Preorder and Inorder Traversal
Given two integer arrays preorder and inorder where:
- preorder is the preorder traversal of a binary tree
- inorder is the inorder traversal of the same tree
Construct and return the binary tree.
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def buildTree(preorder, inorder):
    """
    Build a binary tree from preorder and inorder traversals.

    Args:
        preorder: List[int], preorder traversal
        inorder: List[int], inorder traversal

    Returns:
        TreeNode, root of constructed tree
    """
    if not preorder or not inorder:
        return None

    inorder_map = {val: idx for idx, val in enumerate(inorder)}
    preorder_idx = [0]

    def build(in_start, in_end):
        if in_start > in_end:
            return None

        root_val = preorder[preorder_idx[0]]
        preorder_idx[0] += 1

        in_idx = inorder_map[root_val]
        root = TreeNode(root_val)

        root.left = build(in_start, in_idx - 1)
        root.right = build(in_idx + 1, in_end)

        return root

    return build(0, len(inorder) - 1)


def inorder_traversal(root):
    """Helper to verify tree construction."""
    if not root:
        return []
    return inorder_traversal(root.left) + [root.val] + inorder_traversal(root.right)


def preorder_traversal(root):
    """Helper to verify tree construction."""
    if not root:
        return []
    return [root.val] + preorder_traversal(root.left) + preorder_traversal(root.right)


if __name__ == "__main__":
    # Test case 1
    preorder1 = [3, 9, 20, 15, 7]
    inorder1 = [9, 3, 15, 20, 7]
    root1 = buildTree(preorder1, inorder1)
    assert inorder_traversal(root1) == inorder1
    assert preorder_traversal(root1) == preorder1

    # Test case 2
    preorder2 = [-1]
    inorder2 = [-1]
    root2 = buildTree(preorder2, inorder2)
    assert inorder_traversal(root2) == inorder2
