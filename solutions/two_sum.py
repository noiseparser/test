"""
Two Sum: Given an array of integers and a target, find the two numbers that add up to the target.
Return the indices of the two numbers.
"""


def twoSum(nums, target):
    """
    Find two numbers in nums that add up to target.

    Args:
        nums: List of integers
        target: Target sum

    Returns:
        List of two indices
    """
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []


if __name__ == "__main__":
    assert twoSum([2, 7, 11, 15], 9) == [0, 1]
    assert twoSum([3, 2, 4], 6) == [1, 2]
