from typing import List


def exist(board: List[List[str]], word: str) -> bool:
    """
    Given a 2D board and a word, find if the word exists in the board.
    The word can be constructed from letters of sequentially adjacent cells,
    where adjacent cells are horizontally or vertically neighboring.
    The same letter cell may not be used more than once in a word.

    Uses depth-first search with backtracking.
    Time complexity: O(N * 4^L) where N is board size and L is word length
    Space complexity: O(L) for recursion stack
    """
    if not board or not word:
        return False

    rows, cols = len(board), len(board[0])
    visited = set()

    def dfs(r: int, c: int, index: int) -> bool:
        if index == len(word):
            return True

        if r < 0 or r >= rows or c < 0 or c >= cols:
            return False

        if (r, c) in visited or board[r][c] != word[index]:
            return False

        visited.add((r, c))

        # Try all four directions
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            if dfs(r + dr, c + dc, index + 1):
                return True

        visited.remove((r, c))
        return False

    for i in range(rows):
        for j in range(cols):
            if dfs(i, j, 0):
                return True

    return False


if __name__ == "__main__":
    board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    assert exist(board, "ABCCED") is True
    assert exist(board, "SEE") is True
    assert exist(board, "ABCB") is False
