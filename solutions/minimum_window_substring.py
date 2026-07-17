"""
Minimum Window Substring: Given two strings s and t of lengths m and n respectively, return the minimum window
substring of s such that every character in t (including duplicates) is included in the window.
"""


def minWindow(s: str, t: str) -> str:
    if not s or not t or len(s) < len(t):
        return ""

    dict_t = {}
    for char in t:
        dict_t[char] = dict_t.get(char, 0) + 1

    required = len(dict_t)
    formed = 0

    window_counts = {}

    left = 0
    min_len = float("inf")
    min_left = 0

    for right in range(len(s)):
        char = s[right]
        window_counts[char] = window_counts.get(char, 0) + 1

        if char in dict_t and window_counts[char] == dict_t[char]:
            formed += 1

        while left <= right and formed == required:
            char = s[left]
            if right - left + 1 < min_len:
                min_len = right - left + 1
                min_left = left

            window_counts[char] -= 1
            if char in dict_t and window_counts[char] < dict_t[char]:
                formed -= 1

            left += 1

    return "" if min_len == float("inf") else s[min_left : min_left + min_len]


if __name__ == "__main__":
    assert minWindow("ADOBECODEBANC", "ABC") == "BANC"
    assert minWindow("a", "a") == "a"
    assert minWindow("a", "aa") == ""
