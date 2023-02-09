"""
Exercise: Product of Array Except Self
Difficulty: Medium
Time: 30 min
LeetCode: https://leetcode.com/problems/product-of-array-except-self/
"""

import math


# Time: O(n), Space: O(1), where n is the lenth of the nums array
def solution(nums):
    zeros = nums.count(0)
    # Edge case: More than 1 zeros
    if zeros > 1:
        return [0] * len(nums)

    prod = math.prod(n for n in nums if n)

    # Edge case: Exactly 1 zero
    if zeros == 1:
        return [0 if num != 0 else prod for num in nums]

    return [prod // num for num in nums]
