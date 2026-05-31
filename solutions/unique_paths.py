"""
Unique Paths Problem:
There is an m x n grid. A robot starts at the top-left corner (grid[0][0]).
The robot can only move right or down.
Count the number of unique paths to reach the bottom-right corner.
"""


def uniquePaths(m, n):
    """
    Calculate the number of unique paths in an m x n grid.
    Robot can only move right or down.
    """
    dp = [[1] * n for _ in range(m)]

    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

    return dp[m - 1][n - 1]


if __name__ == "__main__":
    assert uniquePaths(3, 7) == 28
    assert uniquePaths(3, 2) == 3
    assert uniquePaths(1, 1) == 1
