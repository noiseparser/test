"""
Word Break Problem:
Given a string s and a dictionary of strings wordDict,
return True if s can be segmented into a space-separated sequence of dictionary words.
"""


def wordBreak(s, wordDict):
    """
    Determine if string can be broken into dictionary words.
    Uses dynamic programming approach.
    """
    word_set = set(wordDict)
    dp = [False] * (len(s) + 1)
    dp[0] = True

    for i in range(1, len(s) + 1):
        for j in range(i):
            if dp[j] and s[j:i] in word_set:
                dp[i] = True
                break

    return dp[len(s)]


if __name__ == "__main__":
    assert wordBreak("leetcode", ["leet", "code"]) is True
    assert wordBreak("applepenapple", ["apple", "pen"]) is True
    assert wordBreak("catsandog", ["cat", "cats", "and", "sand", "dog"]) is False
