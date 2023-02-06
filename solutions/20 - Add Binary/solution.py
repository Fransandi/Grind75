"""
Exercise: Add Binary
Difficulty: Easy
Time: 15 min
LeetCode: https://leetcode.com/problems/add-binary/
"""


# Time: O(max(a,b)), Space: O(max(a,b)), where a, b are the length of the strings a, b, and max(a, b) is the greatest of them
def solution(a, b):
    solution, carry, base = "", 0, 2
    a, b = list(map(str, a)), list(map(str, b))

    while a or b:
        a_val = int(a.pop()) if a else 0
        b_val = int(b.pop()) if b else 0
        next_sum = a_val + b_val + carry

        carry = 0
        if next_sum >= base:
            carry = 1
            next_sum -= base

        solution = str(next_sum) + solution

    if carry:
        solution = str(carry) + solution

    return solution
