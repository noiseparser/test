"""
You have n rooms labeled from 0 to n-1, and each room may contain keys to
other rooms. Determine if you can visit all rooms starting from room 0.
"""

from typing import List


def canVisitAllRooms(rooms: List[List[int]]) -> bool:
    """
    Check if all rooms are accessible using DFS from room 0.

    Args:
        rooms: List[List[int]] where rooms[i] contains keys to rooms in that list

    Returns:
        bool: True if all rooms can be visited
    """
    visited = set()

    def dfs(room):
        if room in visited:
            return
        visited.add(room)
        for key in rooms[room]:
            dfs(key)

    dfs(0)
    return len(visited) == len(rooms)


if __name__ == "__main__":
    assert canVisitAllRooms([[1], [2], [3], []]) is True
    assert canVisitAllRooms([[1, 3], [3, 0, 6], [6], [4, 6, 7], [4], [6], [4, 5, 8, 9], [7, 5], [4, 8], [7]]) is False
