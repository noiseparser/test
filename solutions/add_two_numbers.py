"""
Add two numbers represented by linked lists.

Problem: You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order, and each of their nodes contains a single digit.
Add the two numbers and return the sum as a linked list.
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(l1, l2):
    """Add two numbers represented as linked lists."""
    dummy = ListNode(0)
    current = dummy
    carry = 0

    while l1 or l2 or carry:
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0

        total = val1 + val2 + carry
        carry = total // 10
        digit = total % 10

        current.next = ListNode(digit)
        current = current.next

        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None

    return dummy.next


if __name__ == "__main__":
    # Test: 342 + 465 = 807
    # represented as [2, 4, 3] and [5, 6, 4]
    l1_n3 = ListNode(3)
    l1_n2 = ListNode(4, l1_n3)
    l1_n1 = ListNode(2, l1_n2)

    l2_n3 = ListNode(4)
    l2_n2 = ListNode(6, l2_n3)
    l2_n1 = ListNode(5, l2_n2)

    result = addTwoNumbers(l1_n1, l2_n1)
    assert result.val == 7
    assert result.next.val == 0
    assert result.next.next.val == 8
