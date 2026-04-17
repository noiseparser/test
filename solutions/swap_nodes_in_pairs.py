"""
Swap nodes in pairs.

Problem: Given a linked list, swap every two adjacent nodes and return its head.
You must solve the problem without modifying the values in the list's nodes.
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def swapPairs(head):
    """Swap every two adjacent nodes iteratively."""
    dummy = ListNode(0)
    dummy.next = head
    prev = dummy

    while prev.next and prev.next.next:
        first = prev.next
        second = prev.next.next

        # Swap
        prev.next = second
        first.next = second.next
        second.next = first

        prev = first

    return dummy.next


if __name__ == "__main__":
    # Test 1: [1, 2, 3, 4] -> [2, 1, 4, 3]
    n4 = ListNode(4)
    n3 = ListNode(3, n4)
    n2 = ListNode(2, n3)
    n1 = ListNode(1, n2)

    result = swapPairs(n1)
    assert result.val == 2
    assert result.next.val == 1
    assert result.next.next.val == 4
    assert result.next.next.next.val == 3

    # Test 2: Single node [1] -> [1]
    single = ListNode(1)
    result2 = swapPairs(single)
    assert result2.val == 1
    assert result2.next is None
