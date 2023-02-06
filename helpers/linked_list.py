"""
Linked List Helper
Collection of classes/methods to help define and parse the input/output expected from LeetCode
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def array_to_linked_list(elements, cycle=-1):
    # Edge case: array is empty
    if len(elements) == 0:
        return ListNode(None)

    head = ListNode(elements.pop(0))
    node = head
    while elements:
        node.next = ListNode(elements.pop(0))
        node = node.next

    if cycle != -1:
        add_cycle_at_the_end(head, node, cycle)

    return head


def linked_list_to_array(head):
    array = []
    while head:
        if head.val:
            array.append(head.val)
        head = head.next
    return array


def add_cycle_at_the_end(head, tail, cycle):
    cycle_node = head
    for _ in range(cycle):
        cycle_node = cycle_node.next
    tail.next = cycle_node
