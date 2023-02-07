"""
Exercise:  Middle of the Linked List
Difficulty: Easy
Time: 20 min
LeetCode: https://leetcode.com/problems/middle-of-the-linked-list/
"""

from helpers import linked_list


# Time: O(n), Space: O(1), where n is the number of nodes in the linked list
def solution(head):
    head = linked_list.array_to_linked_list(head)

    left, right = head, head
    while right and right.next:
        left = left.next
        right = right.next
        if right:
            right = right.next

    return linked_list.linked_list_to_array(left)
