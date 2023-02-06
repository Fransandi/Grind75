"""
Exercise: First Bad Version
Difficulty: Easy
Time: 20 min
LeetCode: https://leetcode.com/problems/first-bad-version/
"""


# Binary Search -> Time: O(log n), Space: O(1), where n is the number of versions n
def solution(n, bad):
    first_bad_version = bad

    def is_bad_version(version: int) -> bool:
        nonlocal first_bad_version
        return version == first_bad_version

    def find_first_bad_version(lower, higher):
        if lower == higher:
            return lower

        mid = (lower + higher) // 2

        if is_bad_version(mid):
            return find_first_bad_version(lower, mid)
        else:
            return find_first_bad_version(mid + 1, higher)

    return find_first_bad_version(0, n)
