"""
Count the number of islands in a grid where 1s represent land and 0s represent water.
An island is formed by connecting adjacent lands horizontally or vertically.
"""


def numIslands(grid):
    """
    Find the number of islands in a 2D grid using DFS.

    Args:
        grid: List[List[str]] where '1' is land and '0' is water

    Returns:
        int: Number of islands
    """
    if not grid or not grid[0]:
        return 0

    rows, cols = len(grid), len(grid[0])
    count = 0

    def dfs(r, c):
        if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == '0':
            return
        grid[r][c] = '0'
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == '1':
                count += 1
                dfs(i, j)

    return count


if __name__ == "__main__":
    grid1 = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ]
    assert numIslands(grid1) == 1

    grid2 = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]
    assert numIslands(grid2) == 3
