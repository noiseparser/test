"""
Rotate Image: Rotate a 2D matrix 90 degrees clockwise in-place.
"""


def rotate(matrix):
    """
    Rotate a 2D matrix 90 degrees clockwise in-place.

    Time complexity: O(n^2)
    Space complexity: O(1)
    """
    n = len(matrix)

    for i in range(n // 2):
        for j in range(i, n - i - 1):
            top = matrix[i][j]
            matrix[i][j] = matrix[n - 1 - j][i]
            matrix[n - 1 - j][i] = matrix[n - 1 - i][n - 1 - j]
            matrix[n - 1 - i][n - 1 - j] = matrix[j][n - 1 - i]
            matrix[j][n - 1 - i] = top


if __name__ == "__main__":
    matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    rotate(matrix1)
    assert matrix1 == [[7, 4, 1], [8, 5, 2], [9, 6, 3]]

    matrix2 = [[1, 2], [3, 4]]
    rotate(matrix2)
    assert matrix2 == [[3, 1], [4, 2]]
