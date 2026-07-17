from typing import List


def permute(nums: List[int]) -> List[List[int]]:
    """
    Generate all permutations of the given array.

    Uses backtracking with a swap-based approach for in-place permutation generation.
    Time complexity: O(n! * n)
    Space complexity: O(n!) for the output
    """
    result = []

    def backtrack(first: int = 0):
        if first == len(nums):
            result.append(nums[:])
            return

        for i in range(first, len(nums)):
            nums[first], nums[i] = nums[i], nums[first]
            backtrack(first + 1)
            nums[first], nums[i] = nums[i], nums[first]

    backtrack()
    return result


def permute_iterative(nums: List[int]) -> List[List[int]]:
    """
    Alternative solution using an iterative approach.
    """
    result = [[]]

    for num in nums:
        new_result = []
        for perm in result:
            for i in range(len(perm) + 1):
                new_result.append(perm[:i] + [num] + perm[i:])
        result = new_result

    return result


if __name__ == "__main__":
    result = permute([1, 2, 3])
    assert len(result) == 6
    assert [1, 2, 3] in result
    assert [3, 2, 1] in result

    result = permute_iterative([1, 2])
    assert len(result) == 2
