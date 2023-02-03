'''
Exercise: Linked List Cycle
Difficulty: Easy
Time: 20 min
LeetCode: https://leetcode.com/problems/linked-list-cycle/
'''

from helpers.linked_list import build_linked_list

def solution(head, pos):
    head = build_linked_list(head, pos)
    visited = set()
    while head:
        # Cycle found
        if head in visited:
            return True

        visited.add(head)
        head = head.next

    return False
