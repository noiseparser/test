"""
Generate Parentheses: Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
"""


def generateParenthesis(n: int) -> list[str]:
    result = []

    def backtrack(open_count, close_count, current):
        if open_count == n and close_count == n:
            result.append(current)
            return

        if open_count < n:
            backtrack(open_count + 1, close_count, current + "(")

        if close_count < open_count:
            backtrack(open_count, close_count + 1, current + ")")

    backtrack(0, 0, "")
    return result


if __name__ == "__main__":
    result = generateParenthesis(3)
    expected = ["((()))", "(()())", "(())()", "()(())", "()()()"]
    assert sorted(result) == sorted(expected)
    assert len(generateParenthesis(1)) == 1
    assert len(generateParenthesis(4)) == 14
