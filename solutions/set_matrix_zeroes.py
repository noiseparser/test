"""
Set Matrix Zeroes: Set entire row and column to zero if element is zero.
"""


def set_zeroes(matrix):
    """
    Set entire row and column to zero if an element is zero, in-place.

    Time complexity: O(m * n)
    Space complexity: O(1)
    """
    if not matrix or not matrix[0]:
        return

    m, n = len(matrix), len(matrix[0])
    first_row_zero = False
    first_col_zero = False

    for i in range(m):
        if matrix[i][0] == 0:
            first_col_zero = True

    for j in range(n):
        if matrix[0][j] == 0:
            first_row_zero = True

    for i in range(1, m):
        for j in range(1, n):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0

    for i in range(1, m):
        for j in range(1, n):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0

    if first_row_zero:
        for j in range(n):
            matrix[0][j] = 0

    if first_col_zero:
        for i in range(m):
            matrix[i][0] = 0


if __name__ == "__main__":
    matrix1 = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    set_zeroes(matrix1)
    assert matrix1 == [[1, 0, 1], [0, 0, 0], [1, 0, 1]]

    matrix2 = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
    set_zeroes(matrix2)
    assert matrix2 == [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]]
