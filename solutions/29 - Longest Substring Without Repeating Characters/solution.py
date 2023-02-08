"""
Exercise: Longest Substring Without Repeating Characters
Difficulty: Medium
Time: 30 min
LeetCode: https://leetcode.com/problems/longest-substring-without-repeating-characters/
"""


# Time: O(n), Space: O(1), where n is the length of the string s
def solution(s):
    i = j = 0
    dic, max_length = set(), 0

    while j < len(s):
        if s[j] not in dic:
            dic.add(s[j])
        else:
            while s[i] != s[j]:
                dic.remove(s[i])
                i += 1
            i += 1

        max_length = max(max_length, len(dic))
        j += 1

    return max_length
