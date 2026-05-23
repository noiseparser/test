"""
House Robber Problem:
You are a professional robber planning to rob houses along a street.
Each house has a certain amount of money stashed.
You cannot rob two adjacent houses.
Return the maximum amount of money you can rob.
"""


def rob(nums):
    """
    Calculate the maximum amount of money that can be robbed
    without robbing two adjacent houses.
    """
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]

    prev2 = 0
    prev1 = nums[0]

    for i in range(1, len(nums)):
        current = max(prev1, prev2 + nums[i])
        prev2 = prev1
        prev1 = current

    return prev1


if __name__ == "__main__":
    assert rob([1, 2, 3, 1]) == 4
    assert rob([2, 7, 9, 3]) == 9
