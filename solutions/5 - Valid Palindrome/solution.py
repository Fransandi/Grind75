"""
Exercise: Valid Palindrome
Difficulty: Easy
Time: 15 min
LeetCode: https://leetcode.com/problems/valid-palindrome/
"""


# Time: O(n), Space: O(n), where n is the length of the s string
def solution(s):
    s = [char.lower() for char in s if char.isalnum()]
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True
