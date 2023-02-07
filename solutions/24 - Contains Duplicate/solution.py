"""
Exercise: Contains Duplicate
Difficulty: Easy
Time: 15 min
LeetCode: https://leetcode.com/problems/contains-duplicate/
"""


# Time: O(n), Space: O(n), where n is the length of the nums array
def solution(nums):
    return len(nums) != len(set(nums))
