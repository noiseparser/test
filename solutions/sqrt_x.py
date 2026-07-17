"""
Sqrt(x).

Given a non-negative integer x, compute and return the square root of x.
Return only the integer part of the result.
"""


def mySqrt(x):
    """
    Compute the integer square root of x using binary search.

    Args:
        x: Non-negative integer

    Returns:
        Integer square root
    """
    if x == 0:
        return 0

    left, right = 1, x

    while left <= right:
        mid = (left + right) // 2
        if mid * mid == x:
            return mid
        elif mid * mid < x:
            left = mid + 1
        else:
            right = mid - 1

    return right


if __name__ == "__main__":
    assert mySqrt(4) == 2
    assert mySqrt(8) == 2
    assert mySqrt(0) == 0
    assert mySqrt(1) == 1
