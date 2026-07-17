from typing import List


def solveNQueens(n: int) -> List[List[str]]:
    """
    Place n queens on an n x n chessboard such that no two queens threaten each other.
    A queen can attack any piece on the same row, column, or diagonal.

    Uses backtracking to explore valid placements.
    Time complexity: O(N!) in the worst case
    Space complexity: O(N) for the recursion stack
    """
    result = []
    col_set = set()
    diag_set = set()
    anti_diag_set = set()

    def backtrack(row: int, current_board: List[List[str]]):
        if row == n:
            result.append(["".join(row_str) for row_str in current_board])
            return

        for col in range(n):
            # Check if position is safe
            if col in col_set or (row - col) in diag_set or (row + col) in anti_diag_set:
                continue

            # Place queen
            current_board[row][col] = "Q"
            col_set.add(col)
            diag_set.add(row - col)
            anti_diag_set.add(row + col)

            # Recurse to next row
            backtrack(row + 1, current_board)

            # Remove queen (backtrack)
            current_board[row][col] = "."
            col_set.remove(col)
            diag_set.remove(row - col)
            anti_diag_set.remove(row + col)

    # Initialize empty board
    board = [["." for _ in range(n)] for _ in range(n)]
    backtrack(0, board)

    return result


if __name__ == "__main__":
    result = solveNQueens(4)
    assert len(result) == 2
    assert result[0][0] == ".Q.."

    result = solveNQueens(1)
    assert len(result) == 1
    assert result[0][0] == "Q"
