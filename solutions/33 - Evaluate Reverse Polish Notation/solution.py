"""
Exercise: Evaluate Reverse Polish Notation
Difficulty: Medium
Time: 30 min
LeetCode: https://leetcode.com/problems/evaluate-reverse-polish-notation/
"""

import math


# Time: O(n), Space: O(n), wheren is the length of the tokens array
def solution(tokens):
    operands = {"+", "-", "*", "/"}
    result = []

    for val in tokens:
        if val in operands:
            num2 = result.pop()
            num1 = result.pop()
            result.append(str(math.trunc(eval(num1 + val + num2))))
        else:
            result.append(val)

    return int(result[0])
