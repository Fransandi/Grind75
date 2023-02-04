"""
Exercise: Reverse Linked List
Difficulty: Easy
Time: 20 min
LeetCode: https://leetcode.com/problems/reverse-linked-list/
"""


from helpers.linked_list import build_linked_list, linked_list_to_array


def solution(head):
    head = build_linked_list(head)

    prev = None
    cur = head

    while cur:
        temp = cur.next
        cur.next = prev
        prev = cur
        cur = temp

    return linked_list_to_array(prev)
