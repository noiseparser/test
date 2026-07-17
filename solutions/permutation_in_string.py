"""
Permutation in String: Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.
"""


def checkInclusion(s1: str, s2: str) -> bool:
    if len(s1) > len(s2):
        return False

    s1_count = {}
    for char in s1:
        s1_count[char] = s1_count.get(char, 0) + 1

    window_count = {}
    for i in range(len(s1)):
        char = s2[i]
        window_count[char] = window_count.get(char, 0) + 1

    if window_count == s1_count:
        return True

    for i in range(len(s1), len(s2)):
        char = s2[i]
        window_count[char] = window_count.get(char, 0) + 1

        left_char = s2[i - len(s1)]
        window_count[left_char] -= 1
        if window_count[left_char] == 0:
            del window_count[left_char]

        if window_count == s1_count:
            return True

    return False


if __name__ == "__main__":
    assert checkInclusion("ab", "eidbaooo") is True
    assert checkInclusion("ab", "ab") is True
    assert checkInclusion("ab", "ba") is True
    assert checkInclusion("abc", "ab") is False
