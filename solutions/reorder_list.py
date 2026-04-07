"""
Reorder a linked list.

Problem: Given the head of a singly linked list L: L0 -> L1 -> ... -> Ln-1 -> Ln,
reorder it to: L0 -> Ln -> L1 -> Ln-1 -> L2 -> Ln-2 -> ...
You may not modify the values in the list's nodes, only nodes itself may be changed.
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reorderList(head):
    """Reorder the list by finding middle, reversing second half, and merging."""
    if not head or not head.next:
        return

    # Find middle
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # Reverse second half
    prev = None
    curr = slow
    while curr:
        next_temp = curr.next
        curr.next = prev
        prev = curr
        curr = next_temp

    # Merge the two halves
    first, second = head, prev
    while second.next:  # second.next check to avoid overwriting
        first_next = first.next
        second_next = second.next

        first.next = second
        second.next = first_next

        first = first_next
        second = second_next


if __name__ == "__main__":
    # Test: [1, 2, 3, 4, 5] -> [1, 5, 2, 4, 3]
    n5 = ListNode(5)
    n4 = ListNode(4, n5)
    n3 = ListNode(3, n4)
    n2 = ListNode(2, n3)
    n1 = ListNode(1, n2)

    reorderList(n1)
    assert n1.val == 1
    assert n1.next.val == 5
    assert n1.next.next.val == 2
    assert n1.next.next.next.val == 4
