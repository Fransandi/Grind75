"""
Exercise: Binary Search
Difficulty: Easy
Time: 15 min
LeetCode: https://leetcode.com/problems/binary-search/
"""


def solution(nums, target):
    left, right = 0, len(nums) - 1

    while left <= right:
        index = (left + right) // 2

        if nums[index] == target:
            return index
        elif nums[index] > target:
            right = index - 1
        else:
            left = index + 1

    return -1
