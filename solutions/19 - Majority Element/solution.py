"""
Exercise: Majority Element
Difficulty: Easy
Time: 20 min
LeetCode: https://leetcode.com/problems/majority-element/
"""

import random
from collections import defaultdict


# Counting -> Time: O(n), Space: O(n)
def solution(nums):
    count = defaultdict(int)

    for num in nums:
        count[num] += 1

        if count[num] > len(nums) // 2:
            return num

    return -1


# Randomization -> Time O(n) or O(inf), Space: O(1)
def solution2(nums):
    checked = set()
    while True:
        random_pos = random.randint(0, len(nums) - 1)
        val = nums[random_pos]

        if val not in checked:
            checked.add(val)

            count = sum([1 for n in nums if n == val])

            if count > len(nums) // 2:
                return val


# Booyer-Moore Algorithm -> Time O(n), Space: O(1)
def solution3(nums):
    candidate = None
    count = 0

    for n in nums:
        if count == 0:
            candidate = n

        count += 1 if n == candidate else -1

    return candidate
