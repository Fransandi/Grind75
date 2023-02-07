"""
Exercise: Maximum Subarray
Difficulty: Easy
Time: 20 min
LeetCode: https://leetcode.com/problems/maximum-subarray/
"""


def solution(nums):
    cur_sum = max_sum = nums[0]

    for i in range(1, len(nums)):
        cur_sum = max(nums[i], cur_sum + nums[i])
        max_sum = max(max_sum, cur_sum)

    return max_sum
