"""
Exercise: Valid Parentheses
Difficulty: Easy
Time: 20 min
LeetCode: https://leetcode.com/problems/valid-parentheses/
"""


# Time: O(n), Space: O(n), where n is the length of the string s
def solution(s) -> bool:
    dict = {"(": ")", "[": "]", "{": "}"}
    stack = []

    for char in s:
        if char in dict.keys():
            stack.append(char)
        elif char in dict.values():
            if not stack or dict[stack.pop()] != char:
                return False
        else:
            return False

    return len(stack) == 0
