"""
Merge Sorted Array.

Merge two sorted integer arrays nums1 and nums2 into a single sorted array.
nums1 has enough space (size m + n) to hold all elements from nums2.
"""


def merge(nums1, m, nums2, n):
    """
    Merge nums2 into nums1 in-place.

    Args:
        nums1: First sorted array with size m + n
        m: Number of valid elements in nums1
        nums2: Second sorted array with size n
        n: Number of elements in nums2
    """
    p1 = m - 1
    p2 = n - 1
    p = m + n - 1

    while p1 >= 0 and p2 >= 0:
        if nums1[p1] > nums2[p2]:
            nums1[p] = nums1[p1]
            p1 -= 1
        else:
            nums1[p] = nums2[p2]
            p2 -= 1
        p -= 1

    # If there are remaining elements in nums2, copy them
    while p2 >= 0:
        nums1[p] = nums2[p2]
        p2 -= 1
        p -= 1


if __name__ == "__main__":
    nums1 = [1, 2, 3, 0, 0, 0]
    merge(nums1, 3, [2, 5, 6], 3)
    assert nums1 == [1, 2, 2, 3, 5, 6]

    nums1_2 = [1]
    merge(nums1_2, 1, [], 0)
    assert nums1_2 == [1]
