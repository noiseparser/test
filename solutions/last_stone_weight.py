import heapq
from typing import List


def lastStoneWeight(stones: List[int]) -> int:
    """
    Simulate a game where stones collide and destroy each other.
    The stone with the heaviest weight wins, and the difference becomes a new stone.
    Return the weight of the last remaining stone, or 0 if no stones remain.

    Uses a max-heap (simulated with negative values).
    Time complexity: O(n log n)
    Space complexity: O(n)
    """
    if not stones:
        return 0

    # Convert to max-heap by negating values
    heap = [-stone for stone in stones]
    heapq.heapify(heap)

    while len(heap) > 1:
        first = -heapq.heappop(heap)
        second = -heapq.heappop(heap)

        if first != second:
            heapq.heappush(heap, -(first - second))

    return -heap[0] if heap else 0


if __name__ == "__main__":
    assert lastStoneWeight([2, 7, 4, 1, 8, 1]) == 1
    assert lastStoneWeight([1]) == 1
    assert lastStoneWeight([1, 1]) == 0
