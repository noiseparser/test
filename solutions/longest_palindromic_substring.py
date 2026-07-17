"""
Longest Palindromic Substring: Find the longest palindromic substring in a string.
"""


def longest_palindrome(s):
    """
    Find the longest palindromic substring using expand around center approach.

    Time complexity: O(n^2)
    Space complexity: O(1) excluding output
    """
    if not s:
        return ""

    def expand_around_center(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]

    longest = ""
    for i in range(len(s)):
        palindrome1 = expand_around_center(i, i)
        palindrome2 = expand_around_center(i, i + 1)

        if len(palindrome1) > len(longest):
            longest = palindrome1
        if len(palindrome2) > len(longest):
            longest = palindrome2

    return longest


if __name__ == "__main__":
    assert longest_palindrome("babad") in ["bab", "aba"]
    assert longest_palindrome("ac") == "a"
    assert longest_palindrome("racecar") == "racecar"
