"""
Exercise: Insert Interval
Difficulty: Medium
Time: 25 min
LeetCode: https://leetcode.com/problems/insert-interval/
"""


# Time: O(n), Space: O(n), where n is the length of the intervals array
def solution(intervals, newInterval):
    merged_intervals = []

    for index in range(len(intervals)):
        start, end = intervals[index]
        new_start, new_end = newInterval

        # New interval is ready to be inserted
        if start > new_end:
            return merged_intervals + [newInterval] + intervals[index:]
        # Current interval is not overlapping
        elif new_start > end:
            merged_intervals.append([start, end])
        # Merge intervals
        else:
            newInterval = [min(start, new_start), max(end, new_end)]

    return merged_intervals + [newInterval]
