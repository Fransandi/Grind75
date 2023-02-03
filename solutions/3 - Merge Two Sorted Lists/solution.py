"""
Exercise: Merge Two Sorted Lists
Difficulty: Easy
Time: 20 min
LeetCode: https://leetcode.com/problems/merge-two-sorted-lists/
"""


def solution(list1, list2):
    res = []
    while list1 and list2:
        res += [list1.pop(0)] if list1[0] < list2[0] else [list2.pop(0)]
    return res + list1 + list2
