"""
Remove Duplicates from Sorted Array.

Remove all duplicates from a sorted array in-place such that each unique element
appears only once. Return the number of unique elements.
"""


def removeDuplicates(nums):
    """
    Remove duplicates from sorted array in-place.

    The array is modified such that the first k elements contain the unique values.

    Args:
        nums: Sorted list of integers

    Returns:
        Number of unique elements (k)
    """
    if not nums:
        return 0

    k = 1
    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:
            nums[k] = nums[i]
            k += 1

    return k


if __name__ == "__main__":
    nums1 = [1, 1, 2]
    assert removeDuplicates(nums1) == 2
    assert nums1[:2] == [1, 2]

    nums2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    assert removeDuplicates(nums2) == 5
    assert nums2[:5] == [0, 1, 2, 3, 4]
