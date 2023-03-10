"""
Exercise: Two Sum
Difficulty: Easy
Time: 15 min
LeetCode: https://leetcode.com/problems/two-sum/
"""


# Time: O(n), Space: O(n), where n is the length of the nums array
def solution(nums, target):
    nums_to_index = {}
    for index, num in enumerate(nums):
        if num in nums_to_index:
            return [nums_to_index[num], index]
        nums_to_index[target - num] = index
