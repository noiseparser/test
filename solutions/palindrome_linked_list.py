"""
Check if a singly linked list is a palindrome.

Problem: Given the head of a singly linked list, determine if the linked list is a palindrome.
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def isPalindrome(head):
    """Check if the linked list is a palindrome using slow/fast pointers and reversal."""
    if not head or not head.next:
        return True

    # Find the middle of the list
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # Reverse the second half
    prev = None
    while slow:
        next_temp = slow.next
        slow.next = prev
        prev = slow
        slow = next_temp

    # Compare first and second half
    left, right = head, prev
    while right:  # right will be shorter or equal
        if left.val != right.val:
            return False
        left = left.next
        right = right.next

    return True


if __name__ == "__main__":
    # Test 1: Palindrome [1, 2, 2, 1]
    n4 = ListNode(1)
    n3 = ListNode(2, n4)
    n2 = ListNode(2, n3)
    n1 = ListNode(1, n2)
    assert isPalindrome(n1) == True

    # Test 2: Not a palindrome [1, 2, 3]
    m3 = ListNode(3)
    m2 = ListNode(2, m3)
    m1 = ListNode(1, m2)
    assert isPalindrome(m1) == False

    # Test 3: Single element [5]
    single = ListNode(5)
    assert isPalindrome(single) == True
