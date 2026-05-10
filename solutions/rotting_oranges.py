"""
In a grid of fresh (1) and rotten (2) oranges, each minute the rotting spreads
to adjacent fresh oranges. Compute the minimum time for all oranges to rot,
or return -1 if impossible.
"""

from typing import List
from collections import deque


def orangesRotting(grid: List[List[int]]) -> int:
    """
    Find minimum time for all oranges to rot using multi-source BFS.

    Args:
        grid: List[List[int]] where 0=empty, 1=fresh, 2=rotten

    Returns:
        int: Minutes until all oranges rot, or -1 if impossible
    """
    rows, cols = len(grid), len(grid[0])
    queue = deque()
    fresh_count = 0
    minutes = 0

    # Find all rotten oranges and count fresh ones
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 2:
                queue.append((i, j, 0))
            elif grid[i][j] == 1:
                fresh_count += 1

    if fresh_count == 0:
        return 0

    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    while queue:
        r, c, time = queue.popleft()
        minutes = time

        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                grid[nr][nc] = 2
                fresh_count -= 1
                queue.append((nr, nc, time + 1))

    return minutes if fresh_count == 0 else -1


if __name__ == "__main__":
    grid1 = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
    assert orangesRotting(grid1) == 4

    grid2 = [[2, 1, 1], [0, 1, 1], [1, 0, 1]]
    assert orangesRotting(grid2) == -1
