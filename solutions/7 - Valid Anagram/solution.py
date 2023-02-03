"""
Exercise: Valid Anagram
Difficulty: Easy
Time: 15 min
LeetCode: https://leetcode.com/problems/valid-anagram/
"""

from collections import defaultdict


def solution(s, t):
    count_s, count_t = defaultdict(int), defaultdict(int)
    for char in s:
        count_s[char] += 1
    for char in t:
        count_t[char] += 1
    return count_s == count_t
