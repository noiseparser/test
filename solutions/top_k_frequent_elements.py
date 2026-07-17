"""
Top K Frequent Elements: Find the k most frequent elements in an array.
"""

from collections import Counter
import heapq


def top_k_frequent(nums, k):
    """
    Find the k most frequent elements using a min heap.

    Time complexity: O(n log k)
    Space complexity: O(n)
    """
    if k == len(nums):
        return nums

    count = Counter(nums)
    return heapq.nlargest(k, count.keys(), key=count.get)


if __name__ == "__main__":
    assert sorted(top_k_frequent([1, 1, 1, 2, 2, 3], 2)) == [1, 2]
    assert sorted(top_k_frequent([4, 1, 1, 1, 2, 2, 3], 2)) == [1, 2]
