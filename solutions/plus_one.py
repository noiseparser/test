"""
Plus One.

Given a non-empty array of digits representing a non-negative integer,
increment the integer by one.
"""


def plusOne(digits):
    """
    Add one to the number represented by the array of digits.

    Args:
        digits: List of digits representing a number

    Returns:
        List of digits after incrementing by one
    """
    for i in range(len(digits) - 1, -1, -1):
        if digits[i] < 9:
            digits[i] += 1
            return digits
        digits[i] = 0

    return [1] + digits


if __name__ == "__main__":
    assert plusOne([1, 2, 3]) == [1, 2, 4]
    assert plusOne([4, 3, 2, 1]) == [4, 3, 2, 2]
    assert plusOne([9]) == [1, 0]
