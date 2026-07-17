"""
Container With Most Water: Find two lines that form a container with maximum area.
"""


def max_area(height):
    """
    Find the maximum area that can be formed by two lines.

    Time complexity: O(n)
    Space complexity: O(1)
    """
    left = 0
    right = len(height) - 1
    max_area_val = 0

    while left < right:
        current_area = min(height[left], height[right]) * (right - left)
        max_area_val = max(max_area_val, current_area)

        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_area_val


if __name__ == "__main__":
    assert max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
    assert max_area([1, 1]) == 1
