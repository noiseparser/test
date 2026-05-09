"""
Determine if you can finish all courses given prerequisites.
A course has prerequisites represented as [course, prerequisite] pairs.
Detect if there is a cycle in the dependency graph.
"""

from typing import List


def canFinish(numCourses: int, prerequisites: List[List[int]]) -> bool:
    """
    Check if all courses can be finished using topological sort with DFS.

    Args:
        numCourses: Number of courses
        prerequisites: List of [course, prerequisite] pairs

    Returns:
        bool: True if all courses can be finished, False if cycle exists
    """
    # 0: unvisited, 1: visiting, 2: visited
    state = [0] * numCourses
    adj = [[] for _ in range(numCourses)]

    # Build adjacency list
    for course, prereq in prerequisites:
        adj[course].append(prereq)

    def has_cycle(node):
        if state[node] == 1:
            return True
        if state[node] == 2:
            return False

        state[node] = 1

        for neighbor in adj[node]:
            if has_cycle(neighbor):
                return True

        state[node] = 2
        return False

    for i in range(numCourses):
        if state[i] == 0:
            if has_cycle(i):
                return False

    return True


if __name__ == "__main__":
    assert canFinish(2, [[1, 0]]) is True
    assert canFinish(2, [[1, 0], [0, 1]]) is False
