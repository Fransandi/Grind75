class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def build_linked_list(elements, cycle=-1):
    head = ListNode([elements.pop(0)])
    node = head
    while elements:
        node.next = ListNode(elements.pop(0))
        node = node.next

    if cycle >= 0:
        cycle_node = head
        for _ in range(cycle):
            cycle_node = cycle_node.next
        node.next = cycle_node
    return head


def linked_list_to_array(head):
    array = []
    while head:
        array.append(head.val)
        head = head.next
    return array
