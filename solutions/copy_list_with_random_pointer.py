"""
Copy a linked list with random pointers.

Problem: A linked list of length n is given such that each node contains an additional
random pointer, which could point to any node in the list, or null.
Construct a deep copy of the list.
"""


class Node:
    def __init__(self, val, next=None, random=None):
        self.val = val
        self.next = next
        self.random = random


def copyRandomList(head):
    """Deep copy a linked list with random pointers using a hash map."""
    if not head:
        return None

    # First pass: create mapping from old nodes to new nodes
    node_map = {}
    curr = head
    while curr:
        node_map[curr] = Node(curr.val)
        curr = curr.next

    # Second pass: set next and random pointers
    curr = head
    while curr:
        if curr.next:
            node_map[curr].next = node_map[curr.next]
        if curr.random:
            node_map[curr].random = node_map[curr.random]
        curr = curr.next

    return node_map[head]


if __name__ == "__main__":
    # Test: Copy list with random pointers
    node1 = Node(1)
    node2 = Node(2)
    node1.next = node2
    node2.next = None
    node1.random = node2
    node2.random = node1

    copy = copyRandomList(node1)
    assert copy.val == 1
    assert copy.next.val == 2
    assert copy.random.val == 2
    assert copy.next.random.val == 1
    assert copy is not node1
    assert copy.next is not node2
