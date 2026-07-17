"""
Find the middle of the linked list.

Problem: Given the head of a singly linked list, find and return the middle node.
If the list has even number of nodes, return the second middle node.
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def middleNode(head):
    """Find the middle node using slow and fast pointers."""
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow


if __name__ == "__main__":
    # Test 1: List with odd length [1, 2, 3, 4, 5]
    n5 = ListNode(5)
    n4 = ListNode(4, n5)
    n3 = ListNode(3, n4)
    n2 = ListNode(2, n3)
    n1 = ListNode(1, n2)

    mid = middleNode(n1)
    assert mid.val == 3

    # Test 2: List with even length [1, 2, 3, 4]
    m4 = ListNode(4)
    m3 = ListNode(3, m4)
    m2 = ListNode(2, m3)
    m1 = ListNode(1, m2)

    mid2 = middleNode(m1)
    assert mid2.val == 3
