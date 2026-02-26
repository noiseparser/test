"""
Detect if a linked list has a cycle.

Use Floyd's cycle detection algorithm (tortoise and hare).
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def hasCycle(head):
    """
    Detect if a linked list has a cycle.

    Args:
        head: Head of the linked list

    Returns:
        True if there is a cycle, False otherwise
    """
    if not head or not head.next:
        return False

    slow = head
    fast = head.next

    while slow != fast:
        if not fast or not fast.next:
            return False
        slow = slow.next
        fast = fast.next.next

    return True


if __name__ == "__main__":
    # Test case 1: List with cycle
    node1 = ListNode(3)
    node2 = ListNode(2)
    node3 = ListNode(0)
    node4 = ListNode(-4)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node2  # cycle

    assert hasCycle(node1) == True

    # Test case 2: List without cycle
    node_a = ListNode(1)
    node_b = ListNode(2)
    node_a.next = node_b

    assert hasCycle(node_a) == False
