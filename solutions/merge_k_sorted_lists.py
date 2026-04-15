"""
Merge k sorted linked lists.

Problem: You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
Merge all the linked-lists into one sorted linked-list and return it.
"""


import heapq


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __lt__(self, other):
        """Compare nodes for heap ordering."""
        return self.val < other.val


def mergeKLists(lists):
    """Merge k sorted lists using a min heap."""
    if not lists:
        return None

    # Create a min heap with the first node of each list
    heap = []
    for list_node in lists:
        if list_node:
            heapq.heappush(heap, (list_node.val, id(list_node), list_node))

    dummy = ListNode(0)
    current = dummy

    while heap:
        val, _, node = heapq.heappop(heap)
        current.next = node
        current = current.next

        if node.next:
            heapq.heappush(heap, (node.next.val, id(node.next), node.next))

    return dummy.next


if __name__ == "__main__":
    # Test: Merge [1, 4, 5], [1, 3, 4], [2, 6]
    list1 = ListNode(1, ListNode(4, ListNode(5)))
    list2 = ListNode(1, ListNode(3, ListNode(4)))
    list3 = ListNode(2, ListNode(6))

    result = mergeKLists([list1, list2, list3])
    expected = [1, 1, 2, 3, 4, 4, 5, 6]

    curr = result
    for exp_val in expected:
        assert curr.val == exp_val
        curr = curr.next
