"""
Daily Temperatures: Given an array of daily temperatures, return an array that, for each day in the input,
tells you how many days you have to wait until a warmer temperature.
"""


def dailyTemperatures(temperatures: list[int]) -> list[int]:
    result = [0] * len(temperatures)
    stack = []

    for i in range(len(temperatures) - 1, -1, -1):
        while stack and temperatures[stack[-1]] <= temperatures[i]:
            stack.pop()

        if stack:
            result[i] = stack[-1] - i

        stack.append(i)

    return result


if __name__ == "__main__":
    assert dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]) == [1, 1, 4, 2, 1, 1, 0, 0]
    assert dailyTemperatures([30, 40, 50, 60]) == [1, 1, 1, 0]
    assert dailyTemperatures([30, 60, 90]) == [1, 1, 0]
