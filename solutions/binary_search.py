"""
Binary Search: Given a sorted array of integers and a target value, find the index
of the target in the array. If the target is not found, return -1. The array is sorted
in ascending order.
"""


def search(nums, target):
    """
    Perform binary search on a sorted array to find target.

    Args:
        nums: Sorted list of integers
        target: Target value to find

    Returns:
        Index of target, or -1 if not found
    """
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


def searchRecursive(nums, target, left=0, right=None):
    """Binary search using recursion."""
    if right is None:
        right = len(nums) - 1

    if left > right:
        return -1

    mid = (left + right) // 2
    if nums[mid] == target:
        return mid
    elif nums[mid] < target:
        return searchRecursive(nums, target, mid + 1, right)
    else:
        return searchRecursive(nums, target, left, mid - 1)


if __name__ == "__main__":
    assert search([-1, 0, 3, 5, 9, 12], 9) == 4
    assert search([-1, 0, 3, 5, 9, 12], 13) == -1
    assert search([1], 1) == 0
    assert searchRecursive([-1, 0, 3, 5, 9, 12], 9) == 4
