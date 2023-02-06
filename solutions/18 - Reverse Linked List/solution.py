"""
Exercise: Reverse Linked List
Difficulty: Easy
Time: 20 min
LeetCode: https://leetcode.com/problems/reverse-linked-list/
"""


from helpers.linked_list import array_to_linked_list, linked_list_to_array


# Time: O(n), Space: O(1), where n is the number of nodes in the linked list
def solution(head):
    head = array_to_linked_list(head)

    prev = None
    cur = head

    while cur:
        temp = cur.next
        cur.next = prev
        prev = cur
        cur = temp

    return linked_list_to_array(prev)
