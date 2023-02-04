"""
Exercise: Longest Palindrome
Difficulty: Easy
Time: 15 min
LeetCode: https://leetcode.com/problems/longest-palindrome/
"""


def solution(s):
    len_palindrome, visited = 0, set()

    for char in s:
        if char in visited:
            visited.remove(char)
            len_palindrome += 2
        else:
            visited.add(char)

    if len(visited):
        len_palindrome += 1

    return len_palindrome
