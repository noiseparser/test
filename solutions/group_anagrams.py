"""
Group Anagrams: Group anagrams from a list of strings.
"""

from collections import defaultdict


def group_anagrams(strs):
    """
    Group anagrams from a list of strings.

    Time complexity: O(n * k log k) where n is number of strings and k is max length
    Space complexity: O(n * k)
    """
    anagram_groups = defaultdict(list)

    for word in strs:
        sorted_word = "".join(sorted(word))
        anagram_groups[sorted_word].append(word)

    return list(anagram_groups.values())


if __name__ == "__main__":
    result = group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    assert sorted([sorted(group) for group in result]) == sorted([
        sorted(["eat", "tea", "ate"]),
        sorted(["tan", "nat"]),
        sorted(["bat"])
    ])
    assert group_anagrams([""]) == [[""]]
