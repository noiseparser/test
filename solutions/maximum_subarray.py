"""
Maximum Subarray: Given an integer array, find the contiguous subarray within it
which has the largest sum. This is also known as the Maximum Sum Subarray Problem
or Kadane's Algorithm.
"""


def maxSubArray(nums):
    """
    Find the maximum sum of any contiguous subarray using Kadane's Algorithm.

    Args:
        nums: List of integers

    Returns:
        Maximum sum of contiguous subarray
    """
    if not nums:
        return 0

    max_current = max_global = nums[0]

    for num in nums[1:]:
        max_current = max(num, max_current + num)
        max_global = max(max_global, max_current)

    return max_global


def maxSubArrayWithTracking(nums):
    """
    Find maximum sum subarray and also return the indices of the subarray.

    Args:
        nums: List of integers

    Returns:
        Tuple of (max_sum, start_index, end_index)
    """
    if not nums:
        return 0, 0, 0

    max_current = max_global = nums[0]
    start = end = temp_start = 0

    for i in range(1, len(nums)):
        if nums[i] > max_current + nums[i]:
            max_current = nums[i]
            temp_start = i
        else:
            max_current = max_current + nums[i]

        if max_current > max_global:
            max_global = max_current
            start = temp_start
            end = i

    return max_global, start, end


if __name__ == "__main__":
    assert maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
    assert maxSubArray([5, 4, -1, 7, 8]) == 23
    assert maxSubArray([-5]) == -5

    result, start, end = maxSubArrayWithTracking([-2, 1, -3, 4, -1, 2, 1, -5, 4])
    assert result == 6
    assert start == 3
    assert end == 6
