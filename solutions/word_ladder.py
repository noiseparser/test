"""
Find the shortest transformation sequence from a start word to an end word.
Each step must change exactly one letter and the intermediate word must
exist in the word list.
"""

from typing import List
from collections import deque


def ladderLength(beginWord: str, endWord: str, wordList: List[str]) -> int:
    """
    Find the shortest word ladder using BFS.

    Args:
        beginWord: Starting word
        endWord: Target word
        wordList: List of valid words

    Returns:
        int: Length of shortest ladder, or 0 if impossible
    """
    word_set = set(wordList)
    if endWord not in word_set:
        return 0

    queue = deque([(beginWord, 1)])
    visited = {beginWord}

    while queue:
        word, level = queue.popleft()

        if word == endWord:
            return level

        for i in range(len(word)):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                new_word = word[:i] + c + word[i + 1:]

                if new_word in word_set and new_word not in visited:
                    if new_word == endWord:
                        return level + 1
                    visited.add(new_word)
                    queue.append((new_word, level + 1))

    return 0


if __name__ == "__main__":
    wordList1 = ["hot", "dot", "dog", "lot", "log", "cog"]
    assert ladderLength("hit", "cog", wordList1) == 5

    wordList2 = ["hot", "dot", "dog", "lot", "log"]
    assert ladderLength("hit", "cog", wordList2) == 0
