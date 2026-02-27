"""
Climbing Stairs.

You are climbing a staircase with n steps. Each time you can climb 1 or 2 steps.
In how many distinct ways can you climb to the top?
"""


def climbStairs(n):
    """
    Calculate the number of distinct ways to climb n stairs.

    Dynamic programming approach: dp[i] = dp[i-1] + dp[i-2]

    Args:
        n: Number of stairs

    Returns:
        Number of distinct ways to climb
    """
    if n == 1:
        return 1
    if n == 2:
        return 2

    prev2 = 1
    prev1 = 2

    for i in range(3, n + 1):
        current = prev1 + prev2
        prev2 = prev1
        prev1 = current

    return prev1


def climbStairs_recursive(n, memo=None):
    """Alternative recursive solution with memoization."""
    if memo is None:
        memo = {}

    if n in memo:
        return memo[n]

    if n == 1:
        return 1
    if n == 2:
        return 2

    memo[n] = climbStairs_recursive(n - 1, memo) + climbStairs_recursive(n - 2, memo)
    return memo[n]


if __name__ == "__main__":
    assert climbStairs(2) == 2
    assert climbStairs(3) == 3
    assert climbStairs(4) == 5
    assert climbStairs_recursive(4) == 5
