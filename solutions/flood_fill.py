"""
Flood Fill: Given an image represented by an m x n integer grid, a starting pixel (sr, sc),
and a new color, perform a flood fill (like the paint bucket tool in an image editor).
"""


def floodFill(image, sr, sc, newColor):
    """
    Perform flood fill starting from (sr, sc) with newColor using DFS.

    Args:
        image: 2D list representing the image
        sr: Starting row
        sc: Starting column
        newColor: New color to fill with

    Returns:
        Modified image after flood fill
    """
    if not image or not image[0]:
        return image

    original_color = image[sr][sc]

    # If the new color is the same as original, no need to fill
    if original_color == newColor:
        return image

    def dfs(r, c):
        """Depth-first search helper."""
        if r < 0 or r >= len(image) or c < 0 or c >= len(image[0]):
            return
        if image[r][c] != original_color:
            return

        image[r][c] = newColor

        # Fill in all 4 directions
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)

    dfs(sr, sc)
    return image


def floodFillBFS(image, sr, sc, newColor):
    """Flood fill using BFS (Breadth-First Search)."""
    if not image or not image[0]:
        return image

    original_color = image[sr][sc]

    if original_color == newColor:
        return image

    from collections import deque
    queue = deque([(sr, sc)])
    image[sr][sc] = newColor

    while queue:
        r, c = queue.popleft()

        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < len(image) and 0 <= nc < len(image[0]) and image[nr][nc] == original_color:
                image[nr][nc] = newColor
                queue.append((nr, nc))

    return image


if __name__ == "__main__":
    img1 = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
    result1 = floodFill(img1, 1, 1, 2)
    assert result1 == [[2, 2, 2], [2, 2, 0], [2, 0, 1]]

    img2 = [[0, 0, 0], [0, 0, 0]]
    result2 = floodFillBFS(img2, 0, 0, 2)
    assert result2 == [[2, 2, 2], [2, 2, 2]]
