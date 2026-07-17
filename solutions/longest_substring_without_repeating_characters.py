"""
Longest Substring Without Repeating Characters: Find the length of the longest substring without repeating characters.
"""


def length_of_longest_substring(s):
    """
    Find the length of the longest substring without repeating characters.

    Time complexity: O(n)
    Space complexity: O(min(n, m)) where m is the character set size
    """
    char_index = {}
    left = 0
    max_len = 0

    for right in range(len(s)):
        if s[right] in char_index and char_index[s[right]] >= left:
            left = char_index[s[right]] + 1
        char_index[s[right]] = right
        max_len = max(max_len, right - left + 1)

    return max_len


if __name__ == "__main__":
    assert length_of_longest_substring("abcabcbb") == 3
    assert length_of_longest_substring("bbbbb") == 1
    assert length_of_longest_substring("pwwkew") == 3
