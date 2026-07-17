"""
Edit Distance Problem (Levenshtein Distance):
Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.
Operations: insert a character, delete a character, or replace a character.
"""


def minDistance(word1, word2):
    """
    Calculate the minimum edit distance between two strings.
    Uses dynamic programming with two-dimensional table.
    """
    m, n = len(word1), len(word2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        dp[i][0] = i

    for j in range(n + 1):
        dp[0][j] = j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])

    return dp[m][n]


if __name__ == "__main__":
    assert minDistance("horse", "ros") == 3
    assert minDistance("intention", "execution") == 5
    assert minDistance("a", "b") == 1
