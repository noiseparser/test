"""
Valid Anagram: Given two strings s and t, determine if they are anagrams of each other.
An anagram is a word or phrase formed by rearranging the letters of another,
typically using all the original letters exactly once.
"""


def isAnagram(s, t):
    """
    Check if two strings are anagrams of each other.

    Args:
        s: First string
        t: Second string

    Returns:
        True if they are anagrams, False otherwise
    """
    # If lengths are different, they cannot be anagrams
    if len(s) != len(t):
        return False

    # Count character frequencies in s
    char_count = {}
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1

    # Check if t has the same character frequencies
    for char in t:
        if char not in char_count:
            return False
        char_count[char] -= 1
        if char_count[char] < 0:
            return False

    return True


# Alternative approach using sorting
def isAnagramSort(s, t):
    """Anagram check using sorting."""
    return sorted(s) == sorted(t)


if __name__ == "__main__":
    assert isAnagram("anagram", "nagaram") == True
    assert isAnagram("rat", "car") == False
    assert isAnagram("ab", "ba") == True
    assert isAnagramSort("anagram", "nagaram") == True
