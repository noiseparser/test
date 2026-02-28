"""
Longest Common Prefix.

Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string.
"""


def longestCommonPrefix(strs):
    """
    Find the longest common prefix among a list of strings.

    Args:
        strs: List of strings

    Returns:
        Longest common prefix string
    """
    if not strs:
        return ""

    for i in range(len(strs[0])):
        char = strs[0][i]
        for s in strs[1:]:
            if i >= len(s) or s[i] != char:
                return strs[0][:i]

    return strs[0]


if __name__ == "__main__":
    assert longestCommonPrefix(["flower", "flow", "flight"]) == "fl"
    assert longestCommonPrefix(["dog", "racecar", "car"]) == ""
    assert longestCommonPrefix(["a"]) == "a"
