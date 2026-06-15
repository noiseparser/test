"""
Largest Rectangle in Histogram: Given an array of integers heights representing the histogram's bar heights,
find the area of the largest rectangle in the histogram.
"""


def largestRectangleArea(heights: list[int]) -> int:
    stack = []
    max_area = 0
    index = 0

    while index < len(heights):
        if not stack or heights[index] >= heights[stack[-1]]:
            stack.append(index)
            index += 1
        else:
            top = stack.pop()
            width = index if not stack else index - stack[-1] - 1
            area = heights[top] * width
            max_area = max(max_area, area)

    while stack:
        top = stack.pop()
        width = index if not stack else index - stack[-1] - 1
        area = heights[top] * width
        max_area = max(max_area, area)

    return max_area


if __name__ == "__main__":
    assert largestRectangleArea([2, 1, 5, 6, 2, 3]) == 10
    assert largestRectangleArea([2]) == 2
    assert largestRectangleArea([0, 9]) == 9
