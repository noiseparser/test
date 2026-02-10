"""
Valid Parentheses: Given a string containing just the characters (, ), {, }, [, and ],
determine if the input string is valid. Valid means open brackets must be closed by
the same type of brackets in the correct order.
"""


def isValid(s):
    """
    Check if the parentheses string is valid.

    Args:
        s: String containing parentheses

    Returns:
        True if valid, False otherwise
    """
    stack = []
    matching = {'(': ')', '{': '}', '[': ']'}

    for char in s:
        if char in matching:
            stack.append(char)
        else:
            if not stack or matching[stack.pop()] != char:
                return False

    return len(stack) == 0


if __name__ == "__main__":
    assert isValid("()") == True
    assert isValid("()[]{}") == True
    assert isValid("([)]") == False
