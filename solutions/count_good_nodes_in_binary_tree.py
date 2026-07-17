"""
Count Good Nodes in Binary Tree
Given a binary tree root, a node is called good if the path from the root to the node contains no nodes with a value greater than node.val.
Return the number of good nodes in the binary tree.
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def goodNodes(root):
    """
    Count the number of good nodes in a binary tree.
    A good node is one where no ancestor has a value greater than the node's value.

    Args:
        root: TreeNode, root of the binary tree

    Returns:
        int, number of good nodes
    """
    count = [0]

    def dfs(node, max_val):
        if not node:
            return

        if node.val >= max_val:
            count[0] += 1
            max_val = node.val

        dfs(node.left, max_val)
        dfs(node.right, max_val)

    dfs(root, float('-inf'))
    return count[0]


if __name__ == "__main__":
    # Test case 1: tree with good nodes
    root1 = TreeNode(3)
    root1.left = TreeNode(1)
    root1.right = TreeNode(4)
    root1.left.left = TreeNode(3)

    assert goodNodes(root1) == 4

    # Test case 2: another tree
    root2 = TreeNode(3)
    root2.left = TreeNode(3)
    root2.right = TreeNode(None)
    root2.left.left = TreeNode(4)
    root2.left.right = TreeNode(2)

    # Correcting test case 2
    root2 = TreeNode(3)
    root2.left = TreeNode(3)
    root2.left.left = TreeNode(4)
    root2.left.right = TreeNode(2)

    assert goodNodes(root2) == 3
