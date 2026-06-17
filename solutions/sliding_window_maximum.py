"""
Sliding Window Maximum: Given an array of integers nums and an integer k, there is a sliding window of size k
which is moving from the very left of the array to the very right. Return an array of the max sliding window.
"""


from collections import deque


def maxSlidingWindow(nums: list[int], k: int) -> list[int]:
    if not nums or k <= 0:
        return []

    deq = deque()
    result = []

    for i in range(len(nums)):
        while deq and deq[0] < i - k + 1:
            deq.popleft()

        while deq and nums[deq[-1]] < nums[i]:
            deq.pop()

        deq.append(i)

        if i >= k - 1:
            result.append(nums[deq[0]])

    return result


if __name__ == "__main__":
    assert maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3) == [3, 3, 5, 5, 6, 7]
    assert maxSlidingWindow([1], 1) == [1]
    assert maxSlidingWindow([1, -1], 1) == [1, -1]
