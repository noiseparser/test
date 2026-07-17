"""
Decode Ways Problem:
A message containing letters from A-Z can be encoded into numbers using the following mapping:
'A' -> 1, 'B' -> 2, ..., 'Z' -> 26.
To decode an encoded message, all digits must be grouped then mapped back into letters.
Given a string s containing only digits, return the number of ways to decode it.
"""


def numDecodings(s):
    """
    Count the number of ways to decode a string of digits.
    Uses dynamic programming approach.
    """
    if not s or s[0] == '0':
        return 0

    dp = [0] * (len(s) + 1)
    dp[0] = 1
    dp[1] = 1

    for i in range(2, len(s) + 1):
        one_digit = int(s[i - 1])
        two_digit = int(s[i - 2:i])

        if one_digit != 0:
            dp[i] += dp[i - 1]

        if 10 <= two_digit <= 26:
            dp[i] += dp[i - 2]

    return dp[len(s)]


if __name__ == "__main__":
    assert numDecodings("12") == 2
    assert numDecodings("226") == 3
    assert numDecodings("06") == 0
    assert numDecodings("0") == 0
