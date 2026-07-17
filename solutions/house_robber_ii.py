"""
House Robber II Problem:
All houses are arranged in a circle.
You cannot rob the first and last house at the same time.
Return the maximum amount of money you can rob.
"""


def rob(nums):
    """
    Calculate max money robbed from circular arrangement of houses.
    Cannot rob adjacent houses or both first and last.
    """
    def rob_linear(houses):
        if not houses:
            return 0
        if len(houses) == 1:
            return houses[0]

        prev2 = 0
        prev1 = houses[0]

        for i in range(1, len(houses)):
            current = max(prev1, prev2 + houses[i])
            prev2 = prev1
            prev1 = current

        return prev1

    if len(nums) == 1:
        return nums[0]

    return max(rob_linear(nums[:-1]), rob_linear(nums[1:]))


if __name__ == "__main__":
    assert rob([1, 2, 3, 1]) == 4
    assert rob([2, 3, 2]) == 3
