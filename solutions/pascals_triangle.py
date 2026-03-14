"""
Pascal's Triangle.

Generate the first numRows of Pascal's triangle.
"""


def generate(numRows):
    """
    Generate Pascal's triangle with numRows rows.

    Each element is the sum of the two elements above it.

    Args:
        numRows: Number of rows to generate

    Returns:
        List of lists representing Pascal's triangle
    """
    if numRows == 0:
        return []

    result = [[1]]

    for i in range(1, numRows):
        prev_row = result[-1]
        new_row = [1]

        for j in range(1, i):
            new_row.append(prev_row[j - 1] + prev_row[j])

        new_row.append(1)
        result.append(new_row)

    return result


if __name__ == "__main__":
    assert generate(1) == [[1]]
    assert generate(2) == [[1], [1, 1]]
    assert generate(5) == [
        [1],
        [1, 1],
        [1, 2, 1],
        [1, 3, 3, 1],
        [1, 4, 6, 4, 1]
    ]
