import heapq
from typing import List


def findKthLargest(nums: List[int], k: int) -> int:
    """
    Find the kth largest element in an unsorted array.

    This solution uses a min-heap of size k to track the k largest elements.
    Time complexity: O(n log k)
    Space complexity: O(k)
    """
    if not nums or k <= 0:
        return -1

    # Create a min-heap with the first k elements
    heap = nums[:k]
    heapq.heapify(heap)

    # Process remaining elements
    for num in nums[k:]:
        if num > heap[0]:
            heapq.heapreplace(heap, num)

    return heap[0]


if __name__ == "__main__":
    assert findKthLargest([3, 2, 1, 5, 6, 4], 2) == 5
    assert findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4) == 4
