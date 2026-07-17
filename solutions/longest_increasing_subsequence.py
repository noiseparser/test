"""
Longest Increasing Subsequence (LIS) Problem:
Given an integer array nums, return the length of the longest strictly increasing subsequence.
"""


def lengthOfLIS(nums):
    """
    Find the length of the longest increasing subsequence.
    Uses dynamic programming with O(n log n) time complexity.
    """
    if not nums:
        return 0

    import bisect

    tails = []

    for num in nums:
        pos = bisect.bisect_left(tails, num)
        if pos == len(tails):
            tails.append(num)
        else:
            tails[pos] = num

    return len(tails)


if __name__ == "__main__":
    assert lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]) == 4
    assert lengthOfLIS([0, 1, 0, 4, 4, 4, 3, 2, 1]) == 3
