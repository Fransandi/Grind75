"""
Exercise: 3Sum
Difficulty: Medium
Time: 30 min
LeetCode: https://leetcode.com/problems/3sum/
"""


# Time: O(n2), Space: O(n), where n s the length of the nums array
def solution(nums):
    nums.sort()
    res = []

    # Edge case: No triplets possible
    if len(nums) < 3:
        return []

    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        left, right = i + 1, len(nums) - 1
        while left < right:
            three_sum = nums[i] + nums[left] + nums[right]

            if three_sum == 0:
                res.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1

                while nums[left] == nums[left - 1] and left < right:
                    left += 1

                while nums[right] == nums[right + 1] and left < right:
                    right -= 1

            elif three_sum < 0:
                left += 1
            else:
                right -= 1

    return res
