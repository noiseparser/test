"""
Coin Change Problem:
Given an integer array coins representing coins of different denominations and an integer amount,
return the fewest number of coins that you need to make up that amount.
"""


def coinChange(coins, amount):
    """
    Return the minimum number of coins needed to make the amount.
    Uses dynamic programming approach.
    """
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0

    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[amount] if dp[amount] != float('inf') else -1


if __name__ == "__main__":
    assert coinChange([1, 2, 5], 5) == 1
    assert coinChange([2], 3) == -1
