from typing import List


def letterCombinations(digits: str) -> List[str]:
    """
    Given a string containing digits 2-9, return all possible letter combinations
    that the number could represent on a phone keypad.

    Uses a mapping of digit to letters and backtracking approach.
    Time complexity: O(4^n) where n is the number of digits
    Space complexity: O(4^n) for the output
    """
    if not digits:
        return []

    mapping = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz"
    }

    result = []

    def backtrack(index: int, current: str):
        if index == len(digits):
            result.append(current)
            return

        digit = digits[index]
        letters = mapping[digit]

        for letter in letters:
            backtrack(index + 1, current + letter)

    backtrack(0, "")
    return result


def letterCombinations_iterative(digits: str) -> List[str]:
    """
    Alternative iterative solution.
    """
    if not digits:
        return []

    mapping = {
        "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
        "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
    }

    result = [""]

    for digit in digits:
        temp = []
        for combo in result:
            for letter in mapping[digit]:
                temp.append(combo + letter)
        result = temp

    return result


if __name__ == "__main__":
    result = letterCombinations("23")
    assert len(result) == 6
    assert "ad" in result
    assert "cf" in result

    result = letterCombinations_iterative("234")
    assert len(result) == 18
