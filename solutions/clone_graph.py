"""
Create a deep copy of an undirected graph. Each node in the graph contains
a value and a list of its neighbors.
"""

from collections import defaultdict
from typing import Optional


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


def cloneGraph(node: Optional[Node]) -> Optional[Node]:
    """
    Create a deep copy of a graph using DFS and a visited map.

    Args:
        node: The starting node of the graph

    Returns:
        Optional[Node]: The cloned graph node
    """
    if not node:
        return None

    visited = {}

    def dfs(original):
        if original in visited:
            return visited[original]

        clone = Node(original.val)
        visited[original] = clone

        for neighbor in original.neighbors:
            clone.neighbors.append(dfs(neighbor))

        return clone

    return dfs(node)


if __name__ == "__main__":
    # Test case 1: Single node
    node1 = Node(1)
    cloned1 = cloneGraph(node1)
    assert cloned1.val == 1
    assert cloned1 is not node1

    # Test case 2: Empty graph
    assert cloneGraph(None) is None
