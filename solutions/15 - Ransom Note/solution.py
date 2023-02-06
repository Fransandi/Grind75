"""
Exercise: Ransom Note
Difficulty: Easy
Time: 15 min
LeetCode: https://leetcode.com/problems/ransom-note/
"""


from collections import defaultdict


# Time: O(n+m), Space: O(n), where n, m are the length of the ransomNote and magazine
def solution(ransomNote, magazine):
    dic = defaultdict(int)

    for char in magazine:
        dic[char] += 1

    for char in ransomNote:
        dic[char] -= 1

        if dic[char] < 0:
            return False

    return True
