"""
Exercise:  Climbing Stairs
Difficulty: Easy
Time: 20 min
LeetCode: https://leetcode.com/problems/climbing-stairs/
"""

from functools import lru_cache


# Solution 1: using functools lru_cache -> Time: O(n), Space: O(n), where n is the number of stairs n, using memoization
@lru_cache
def solution(n):
    # Base case: n is 1 or 2
    if n <= 2:
        return n

    return solution(n - 1) + solution(n - 2)


# Solution 2: Manually handled cache -> Time: O(n), Space: O(n), where n is the number of stairs n, using memoization
def solution2(n):
    return solution2_helper(n, {})


def solution2_helper(n, cache):
    # Check cache first for a precomputed solution
    if n in cache:
        return cache[n]

    # Base case: n is 1 or 2
    if n <= 2:
        return n

    cache[n] = solution2_helper(n - 1, cache) + solution2_helper(n - 2, cache)
    return cache[n]
