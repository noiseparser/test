"""
Reverse a singly linked list.

Problem: Given a singly linked list, reverse it and return the new head.
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseList(head):
    """Reverse the linked list iteratively."""
    prev = None
    curr = head
    while curr:
        next_temp = curr.next
        curr.next = prev
        prev = curr
        curr = next_temp
    return prev


if __name__ == "__main__":
    # Test 1: Simple list [1, 2, 3]
    node3 = ListNode(3)
    node2 = ListNode(2, node3)
    node1 = ListNode(1, node2)

    result = reverseList(node1)
    assert result.val == 3
    assert result.next.val == 2
    assert result.next.next.val == 1

    # Test 2: Single node
    single = ListNode(5)
    result2 = reverseList(single)
    assert result2.val == 5
    assert result2.next is None
