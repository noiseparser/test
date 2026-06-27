import heapq


class MedianFinder:
    """
    Find the median of a stream of integers as they arrive.

    Uses two heaps: a max-heap for the smaller half and a min-heap for the larger half.
    Time complexity: O(log n) for addNum, O(1) for findMedian
    Space complexity: O(n)
    """

    def __init__(self):
        self.small = []  # Max-heap (inverted using negative values)
        self.large = []  # Min-heap
        self.small_size = 0
        self.large_size = 0

    def addNum(self, num: int) -> None:
        # Always add to small first
        heapq.heappush(self.small, -num)
        self.small_size += 1

        # Ensure small_size <= large_size + 1
        if self.small_size > self.large_size + 1:
            val = -heapq.heappop(self.small)
            self.small_size -= 1
            heapq.heappush(self.large, val)
            self.large_size += 1

        # Ensure elements in small are <= elements in large
        if self.large_size > 0 and -self.small[0] > self.large[0]:
            small_max = -heapq.heappop(self.small)
            self.small_size -= 1
            large_min = heapq.heappop(self.large)
            self.large_size -= 1

            heapq.heappush(self.small, -large_min)
            self.small_size += 1
            heapq.heappush(self.large, small_max)
            self.large_size += 1

    def findMedian(self) -> float:
        if self.small_size > self.large_size:
            return float(-self.small[0])
        return (-self.small[0] + self.large[0]) / 2.0


if __name__ == "__main__":
    mf = MedianFinder()
    mf.addNum(1)
    assert mf.findMedian() == 1.0
    mf.addNum(2)
    assert mf.findMedian() == 1.5
    mf.addNum(3)
    assert mf.findMedian() == 2.0
