"""
Combination Sum Problem:
Given an array of distinct integers candidates and a target integer target,
return all unique combinations of candidates where the chosen numbers sum to target.
The same number may be chosen from candidates an unlimited number of times.
"""


def combinationSum(candidates, target):
    """
    Find all combinations that sum to target.
    Uses recursive backtracking approach.
    """
    result = []

    def backtrack(start, path, remaining):
        if remaining == 0:
            result.append(path[:])
            return

        if remaining < 0:
            return

        for i in range(start, len(candidates)):
            path.append(candidates[i])
            backtrack(i, path, remaining - candidates[i])
            path.pop()

    backtrack(0, [], target)
    return result


if __name__ == "__main__":
    result = combinationSum([2, 3, 6, 7], 7)
    assert [2, 2, 3] in result and [7] in result
    assert len(result) == 2
    assert combinationSum([2], 1) == []
