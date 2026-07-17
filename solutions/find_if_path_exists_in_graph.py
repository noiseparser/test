"""
Given a directed acyclic graph represented by edges, determine if there
exists a path from source to destination vertex.
"""

from typing import List


def validPath(n: int, edges: List[List[int]], source: int, destination: int) -> bool:
    """
    Check if path exists from source to destination using DFS.

    Args:
        n: Number of vertices (0 to n-1)
        edges: List of directed edges [from, to]
        source: Starting vertex
        destination: Target vertex

    Returns:
        bool: True if path exists
    """
    if source == destination:
        return True

    # Build adjacency list
    graph = [[] for _ in range(n)]
    for u, v in edges:
        graph[u].append(v)

    visited = set()

    def dfs(node):
        if node in visited:
            return False
        if node == destination:
            return True

        visited.add(node)

        for neighbor in graph[node]:
            if dfs(neighbor):
                return True

        return False

    return dfs(source)


if __name__ == "__main__":
    edges1 = [[4, 3], [1, 4], [3, 2], [4, 8], [1, 7], [6, 4], [4, 2], [7, 4], [2, 8], [0, 7], [0, 8]]
    assert validPath(10, edges1, 5, 5) is True

    edges2 = [[4, 3], [1, 4], [4, 8], [1, 7], [6, 4], [4, 2], [7, 4], [2, 8], [0, 7], [0, 8]]
    assert validPath(10, edges2, 5, 9) is False
