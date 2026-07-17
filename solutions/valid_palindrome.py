"""
Valid Palindrome: Given a string, determine if it is a palindrome, considering only
alphanumeric characters and ignoring cases. Spaces and special characters are ignored.
"""


def isPalindrome(s):
    """
    Check if a string is a valid palindrome (alphanumeric only, case-insensitive).

    Args:
        s: String to check

    Returns:
        True if valid palindrome, False otherwise
    """
    # Filter to alphanumeric characters and convert to lowercase
    filtered = ''.join(char.lower() for char in s if char.isalnum())

    # Check if filtered string equals its reverse
    return filtered == filtered[::-1]


# Alternative approach using two pointers
def isPalindromeAlternative(s):
    """Two pointer approach without creating new string."""
    left, right = 0, len(s) - 1

    while left < right:
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1

        if s[left].lower() != s[right].lower():
            return False

        left += 1
        right -= 1

    return True


if __name__ == "__main__":
    assert isPalindrome("A man, a plan, a canal: Panama") == True
    assert isPalindrome("race a car") == False
    assert isPalindrome(" ") == True
    assert isPalindromeAlternative("A man, a plan, a canal: Panama") == True
