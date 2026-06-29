import heapq
from typing import List


def kClosest(points: List[List[int]], k: int) -> List[List[int]]:
    """
    Find k closest points to the origin (0, 0).

    Uses a max-heap to track k closest points.
    Time complexity: O(n log k)
    Space complexity: O(k)
    """
    def distance_sq(point):
        return point[0] ** 2 + point[1] ** 2

    # Create a heap with negative distances to simulate max-heap
    # Store tuples of (-distance_squared, index, point)
    max_heap = []

    for i, point in enumerate(points):
        dist_sq = distance_sq(point)
        if len(max_heap) < k:
            heapq.heappush(max_heap, (-dist_sq, i, point))
        elif dist_sq < -max_heap[0][0]:
            heapq.heapreplace(max_heap, (-dist_sq, i, point))

    return [point for _, _, point in max_heap]


if __name__ == "__main__":
    result = kClosest([[1, 3], [-2, 2], [5, 8]], 2)
    assert len(result) == 2
    assert [1, 3] in result or [-2, 2] in result

    result = kClosest([[3, 3], [5, -1], [-2, 4]], 2)
    assert len(result) == 2
