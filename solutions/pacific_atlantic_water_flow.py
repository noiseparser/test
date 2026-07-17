"""
Find all cells in a grid where water can flow to both Pacific and Atlantic oceans.
Water flows from higher to lower elevations. The top/left edges touch the Pacific,
the bottom/right edges touch the Atlantic.
"""

from typing import List


def pacificAtlantic(heights: List[List[int]]) -> List[List[int]]:
    """
    Find cells that can reach both oceans using reverse DFS from edges.

    Args:
        heights: List[List[int]] representing elevation map

    Returns:
        List[List[int]]: Cells that can reach both oceans
    """
    if not heights or not heights[0]:
        return []

    rows, cols = len(heights), len(heights[0])
    pacific_reachable = set()
    atlantic_reachable = set()

    def dfs(r, c, ocean_set, prev_height):
        if (r < 0 or r >= rows or c < 0 or c >= cols or
                (r, c) in ocean_set or heights[r][c] < prev_height):
            return

        ocean_set.add((r, c))

        dfs(r + 1, c, ocean_set, heights[r][c])
        dfs(r - 1, c, ocean_set, heights[r][c])
        dfs(r, c + 1, ocean_set, heights[r][c])
        dfs(r, c - 1, ocean_set, heights[r][c])

    # DFS from Pacific edges (top, left)
    for i in range(rows):
        dfs(i, 0, pacific_reachable, 0)
    for j in range(cols):
        dfs(0, j, pacific_reachable, 0)

    # DFS from Atlantic edges (bottom, right)
    for i in range(rows):
        dfs(i, cols - 1, atlantic_reachable, 0)
    for j in range(cols):
        dfs(rows - 1, j, atlantic_reachable, 0)

    result = []
    for i in range(rows):
        for j in range(cols):
            if (i, j) in pacific_reachable and (i, j) in atlantic_reachable:
                result.append([i, j])

    return result


if __name__ == "__main__":
    heights1 = [
        [4, 2, 7, 3, 4],
        [7, 4, 6, 5, 8],
        [2, 5, 8, 7, 6],
        [3, 5, 1, 8, 3],
        [3, 2, 7, 4, 5]
    ]
    result1 = pacificAtlantic(heights1)
    assert len(result1) == 7

    heights2 = [[1]]
    result2 = pacificAtlantic(heights2)
    assert len(result2) == 1
