"""
Roman to Integer.

Convert a roman numeral to an integer.
"""


def romanToInt(s):
    """
    Convert a Roman numeral string to its integer value.

    Args:
        s: Roman numeral string

    Returns:
        Integer value
    """
    roman_values = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    total = 0
    prev_value = 0

    for char in reversed(s):
        value = roman_values[char]

        if value < prev_value:
            total -= value
        else:
            total += value

        prev_value = value

    return total


if __name__ == "__main__":
    assert romanToInt("III") == 3
    assert romanToInt("LVIII") == 58
    assert romanToInt("MCMXCIV") == 1994
