"""
Exercise: Ransom Note
Difficulty: Easy
Time: 15 min
LeetCode: https://leetcode.com/problems/ransom-note/
"""


from collections import defaultdict


def solution(ransomNote, magazine):
    dic = defaultdict(int)

    for char in magazine:
        dic[char] += 1

    for char in ransomNote:
        if dic[char] == 0:
            return False
        dic[char] -= 1

    return True
