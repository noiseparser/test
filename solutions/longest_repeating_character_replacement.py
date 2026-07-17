"""
Longest Repeating Character Replacement: You are given a string s and an integer k. You can choose any character
of the string and replace it with any other uppercase English character. Find the length of the longest substring
containing the same letter you can get after performing at most k operations.
"""


def characterReplacement(s: str, k: int) -> int:
    char_count = {}
    left = 0
    max_length = 0

    for right in range(len(s)):
        char_count[s[right]] = char_count.get(s[right], 0) + 1

        max_freq = max(char_count.values())

        while (right - left + 1) - max_freq > k:
            char_count[s[left]] -= 1
            if char_count[s[left]] == 0:
                del char_count[s[left]]
            left += 1
            max_freq = max(char_count.values()) if char_count else 0

        max_length = max(max_length, right - left + 1)

    return max_length


if __name__ == "__main__":
    assert characterReplacement("ABAB", 2) == 4
    assert characterReplacement("ABAB", 0) == 1
    assert characterReplacement("AABCCCCCCCD", 2) == 9
    assert characterReplacement("", 2) == 0
