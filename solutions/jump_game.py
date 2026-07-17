"""
Jump Game Problem:
Given an integer array nums where you are initially positioned at the array's first index,
each element represents your maximum jump length from that position.
Determine if you can reach the last index of the array.
"""


def canJump(nums):
    """
    Determine if we can reach the last index.
    Uses greedy approach tracking the maximum reachable index.
    """
    max_reach = 0

    for i in range(len(nums)):
        if i > max_reach:
            return False

        max_reach = max(max_reach, i + nums[i])

        if max_reach >= len(nums) - 1:
            return True

    return True


if __name__ == "__main__":
    assert canJump([2, 3, 1, 1, 4]) is True
    assert canJump([3, 2, 1, 0, 4]) is False
    assert canJump([0]) is True
