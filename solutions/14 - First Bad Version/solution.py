"""
Exercise: First Bad Version
Difficulty: Easy
Time: 20 min
LeetCode: https://leetcode.com/problems/first-bad-version/
"""

FIRST_BAD_VERSION = None


def solution(n, bad):
    global FIRST_BAD_VERSION
    FIRST_BAD_VERSION = bad
    return helper(0, n)


def isBadVersion(version: int) -> bool:
    return version == FIRST_BAD_VERSION


def helper(lower, higher):
    if lower == higher:
        return lower

    mid = (lower + higher) // 2

    if isBadVersion(mid):
        return helper(lower, mid)
    else:
        return helper(mid + 1, higher)
