"""
Product of Array Except Self: Compute product of array excluding element at each index.
"""


def product_except_self(nums):
    """
    Compute product of array except element at each index.
    Must run in O(n) without using division.

    Time complexity: O(n)
    Space complexity: O(1) excluding output
    """
    n = len(nums)
    result = [1] * n

    prefix = 1
    for i in range(n):
        result[i] = prefix
        prefix *= nums[i]

    suffix = 1
    for i in range(n - 1, -1, -1):
        result[i] *= suffix
        suffix *= nums[i]

    return result


if __name__ == "__main__":
    assert product_except_self([1, 2, 3, 4]) == [24, 12, 8, 6]
    assert product_except_self([2, 3, 4, 5]) == [60, 40, 30, 24]
