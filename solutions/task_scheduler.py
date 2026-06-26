from collections import Counter
from typing import List


def leastInterval(tasks: List[str], n: int) -> int:
    """
    Given a list of tasks and an interval n, return the minimum time to complete all tasks.
    Between two identical tasks, there must be at least n units of time.

    Uses a greedy approach with a priority queue (max-heap simulation).
    Time complexity: O(n)
    Space complexity: O(1) - at most 26 unique letters
    """
    if not tasks:
        return 0

    # Count frequency of each task
    task_counts = Counter(tasks)

    # Get the maximum frequency
    max_freq = max(task_counts.values())

    # Number of tasks with maximum frequency
    max_count = sum(1 for count in task_counts.values() if count == max_freq)

    # Calculate minimum intervals
    min_time = (max_freq - 1) * (n + 1) + max_count

    # The actual time is at least the number of tasks
    return max(min_time, len(tasks))


if __name__ == "__main__":
    assert leastInterval(["A", "A", "A", "B", "B", "B"], 2) == 8
    assert leastInterval(["A", "B", "A"], 0) == 3
