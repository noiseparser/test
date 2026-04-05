"""
Remove the Nth node from the end of a list.

Problem: Given the head of a linked list, remove the nth node from the end of the list
and return the head of the list.
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def removeNthFromEnd(head, n):
    """Remove nth node from end using two pointers."""
    # Create a dummy node to handle edge cases
    dummy = ListNode(0)
    dummy.next = head
    first = dummy
    second = dummy

    # Move first pointer n+1 steps ahead
    for i in range(n + 1):
        if first is None:
            return head
        first = first.next

    # Move both pointers until first reaches the end
    while first:
        first = first.next
        second = second.next

    # Remove the nth node
    second.next = second.next.next

    return dummy.next


if __name__ == "__main__":
    # Test 1: Remove 2nd node from end in [1, 2, 3, 4, 5]
    n5 = ListNode(5)
    n4 = ListNode(4, n5)
    n3 = ListNode(3, n4)
    n2 = ListNode(2, n3)
    n1 = ListNode(1, n2)

    result = removeNthFromEnd(n1, 2)
    assert result.val == 1
    assert result.next.val == 2
    assert result.next.next.val == 3
    assert result.next.next.next.val == 5

    # Test 2: Remove head from single node list
    single = ListNode(1)
    result2 = removeNthFromEnd(single, 1)
    assert result2 is None
