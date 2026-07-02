from typing import List


def subsets(nums: List[int]) -> List[List[int]]:
    """
    Generate all possible subsets of the given array.
    Also known as the power set.

    Uses an iterative approach building subsets incrementally.
    Time complexity: O(n * 2^n)
    Space complexity: O(2^n) for the output
    """
    result = [[]]

    for num in nums:
        result += [curr + [num] for curr in result]

    return result


def subsets_backtrack(nums: List[int]) -> List[List[int]]:
    """
    Alternative solution using backtracking.
    """
    result = []

    def backtrack(start: int, path: List[int]):
        result.append(path[:])
        for i in range(start, len(nums)):
            path.append(nums[i])
            backtrack(i + 1, path)
            path.pop()

    backtrack(0, [])
    return result


if __name__ == "__main__":
    result = subsets([1, 2, 3])
    assert len(result) == 8
    assert [] in result
    assert [1, 2, 3] in result

    result = subsets_backtrack([1, 2])
    assert len(result) == 4
