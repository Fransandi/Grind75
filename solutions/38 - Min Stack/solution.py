"""
Exercise: Min Stack
Difficulty: Medium
Time: 20 min
LeetCode: https://leetcode.com/problems/min-stack/
"""


class MinStack:
    def __init__(self):
        self.min_stack = []
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.min_stack.append(min(val, self.getMin()))

    def pop(self) -> None:
        self.min_stack.pop()
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        if len(self.min_stack):
            return self.min_stack[-1]

        return float("inf")


# Time: O(1), Space: O(n), where n is the lengt of the elements in the array
def solution(instructions):
    min_stack, result = None, []
    for i in range(len(instructions[0])):
        instruction, val = instructions[0][i], instructions[1][i]
        res = None

        if instruction == "MinStack":
            min_stack = MinStack()
        if instruction == "push":
            min_stack.push(val[0])
        if instruction == "pop":
            min_stack.pop()
        if instruction == "top":
            res = min_stack.top()
        if instruction == "getMin":
            res = min_stack.getMin()

        result.append(res)

    return result
