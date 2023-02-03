class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def build_linked_list(elements, pos=-1):
    head = ListNode([elements.pop(0)])
    node = head
    while elements:
        node.next = ListNode(elements.pop(0))
        node = node.next

    if pos >= 0:
        cycle_node = head
        for _ in range(pos):
            cycle_node = cycle_node.next
        node.next = cycle_node
    return head
