"""
Exercise:  Climbing Stairs
Difficulty: Easy
Time: 20 min
LeetCode: https://leetcode.com/problems/climbing-stairs/
"""

from functools import lru_cache


@lru_cache
def solution(n):
    # Base case: n is 1 or 2
    if n <= 2:
        return n

    return solution(n - 1) + solution(n - 2)


"""
# Manually handled cache

def solution2(n):
    return helper(n, {})


def helper(n, cache):
    # Check cache first for a precomputed solution
    if n in cache:
        return cache[n]

    # Base case: n is 1 or 2
    if n <= 2:
        return n

    cache[n] = helper(n - 1, cache) + helper(n - 2, cache)
    return cache[n]
"""
