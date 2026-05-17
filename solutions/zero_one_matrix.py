"""
Given a matrix containing only 0s and 1s, find the distance of each cell
to the nearest 0. Distance is Manhattan distance.
"""

from typing import List
from collections import deque


def updateMatrix(mat: List[List[int]]) -> List[List[int]]:
    """
    Find distance of each cell to nearest 0 using multi-source BFS.

    Args:
        mat: List[List[int]] containing 0s and 1s

    Returns:
        List[List[int]]: Distance matrix
    """
    if not mat or not mat[0]:
        return mat

    rows, cols = len(mat), len(mat[0])
    queue = deque()
    visited = [[False] * cols for _ in range(rows)]

    # Initialize queue with all 0s
    for i in range(rows):
        for j in range(cols):
            if mat[i][j] == 0:
                queue.append((i, j))
                visited[i][j] = True

    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    while queue:
        r, c = queue.popleft()

        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and not visited[nr][nc]:
                visited[nr][nc] = True
                mat[nr][nc] = mat[r][c] + 1
                queue.append((nr, nc))

    return mat


if __name__ == "__main__":
    mat1 = [[0, 0, 0], [0, 1, 0], [1, 1, 1]]
    result1 = updateMatrix(mat1)
    assert result1[1][1] == 1

    mat2 = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    result2 = updateMatrix(mat2)
    assert result2[1][1] == 1
