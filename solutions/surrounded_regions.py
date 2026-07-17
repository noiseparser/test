"""
Capture all 'O' regions that are surrounded by 'X' on the board.
A region that is not surrounded by 'X' is any region that reaches the boundary
of the board. Modify the board in-place to replace surrounded 'O's with 'X's.
"""

from typing import List


def solve(board: List[List[str]]) -> None:
    """
    Capture surrounded regions by finding O's connected to boundary, marking
    others as X using DFS.

    Args:
        board: List[List[str]] representing the board with 'X' and 'O'
    """
    if not board or not board[0]:
        return

    rows, cols = len(board), len(board[0])

    def dfs(r, c):
        if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != 'O':
            return
        board[r][c] = 'V'  # Mark as visited (boundary-connected)
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)

    # Mark all O's connected to boundary
    for i in range(rows):
        if board[i][0] == 'O':
            dfs(i, 0)
        if board[i][cols - 1] == 'O':
            dfs(i, cols - 1)

    for j in range(cols):
        if board[0][j] == 'O':
            dfs(0, j)
        if board[rows - 1][j] == 'O':
            dfs(rows - 1, j)

    # Replace surrounded O's with X's, restore boundary-connected O's
    for i in range(rows):
        for j in range(cols):
            if board[i][j] == 'O':
                board[i][j] = 'X'
            elif board[i][j] == 'V':
                board[i][j] = 'O'


if __name__ == "__main__":
    board1 = [
        ["X", "X", "X", "X"],
        ["X", "O", "O", "X"],
        ["X", "X", "O", "X"],
        ["X", "O", "X", "X"]
    ]
    solve(board1)
    assert board1[1][1] == 'X'

    board2 = [["X"]]
    solve(board2)
    assert board2[0][0] == 'X'
