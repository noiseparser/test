"""
Merge Two Sorted Lists: Merge two sorted linked lists into one sorted linked list.
The new list is made by splicing together the nodes of the two lists.
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(list1, list2):
    """
    Merge two sorted linked lists into one sorted list.

    Args:
        list1: First sorted linked list
        list2: Second sorted linked list

    Returns:
        Head of merged sorted linked list
    """
    dummy = ListNode(0)
    current = dummy

    while list1 and list2:
        if list1.val <= list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next

    current.next = list1 if list1 else list2
    return dummy.next


def list_to_array(node):
    """Helper to convert linked list to array for testing."""
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result


if __name__ == "__main__":
    list1 = ListNode(1, ListNode(2, ListNode(4)))
    list2 = ListNode(1, ListNode(3, ListNode(4)))
    merged = mergeTwoLists(list1, list2)
    assert list_to_array(merged) == [1, 1, 2, 3, 4]

    assert mergeTwoLists(None, None) is None
