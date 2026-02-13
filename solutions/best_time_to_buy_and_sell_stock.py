"""
Best Time to Buy and Sell Stock: You are given an array of integers where each element
represents the stock price on a given day. You may complete at most one transaction.
Find the maximum profit. If you can't make any profit, return 0.
"""


def maxProfit(prices):
    """
    Find the maximum profit from buying and selling a stock once.

    Args:
        prices: List of integers representing daily prices

    Returns:
        Maximum profit possible
    """
    if not prices or len(prices) < 2:
        return 0

    min_price = prices[0]
    max_profit = 0

    for price in prices[1:]:
        profit = price - min_price
        max_profit = max(max_profit, profit)
        min_price = min(min_price, price)

    return max_profit


if __name__ == "__main__":
    assert maxProfit([7, 1, 5, 3, 6, 4]) == 5
    assert maxProfit([7, 6, 4, 3, 1]) == 0
    assert maxProfit([2, 4, 1, 7, 5, 11]) == 10
