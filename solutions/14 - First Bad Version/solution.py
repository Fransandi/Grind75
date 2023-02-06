"""
Exercise: First Bad Version
Difficulty: Easy
Time: 20 min
LeetCode: https://leetcode.com/problems/first-bad-version/
"""

FIRST_BAD_VERSION = None


def initialize_bad_version(bad):
    global FIRST_BAD_VERSION
    FIRST_BAD_VERSION = bad


def isBadVersion(version: int) -> bool:
    return version == FIRST_BAD_VERSION


# Binary Search -> Time: O(log n), Space: O(1), where n is the number of versions n
def solution(n, bad):
    initialize_bad_version(bad)
    return find_first_bad_version(0, n)


def find_first_bad_version(lower, higher):
    if lower == higher:
        return lower

    mid = (lower + higher) // 2

    if isBadVersion(mid):
        return find_first_bad_version(lower, mid)
    else:
        return find_first_bad_version(mid + 1, higher)
