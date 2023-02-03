"""
Exercise: Valid Palindrome
Difficulty: Easy
Time: 15 min
LeetCode: https://leetcode.com/problems/valid-palindrome/
"""


def solution(s):
    clean_string = [char.lower() for char in s if char.isalnum()]
    left, right = 0, len(clean_string) - 1
    while left < right:
        if clean_string[left] != clean_string[right]:
            return False
        left += 1
        right -= 1
    return True
