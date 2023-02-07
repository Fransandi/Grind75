"""
Exercise: Implement Queue using Stacks 
Difficulty: Easy
Time: 20 min
LeetCode: https://leetcode.com/problems/implement-queue-using-stacks/
"""


# Time: O(1), Space: O(n), where n is the number of elements in the queue, approach to amortize methods
class MyQueue:
    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def push(self, el):
        self.in_stack.append(el)

    def pop(self):
        self.peek()
        return self.out_stack.pop()

    def peek(self):
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        return self.out_stack[-1]

    def empty(self):
        return len(self.in_stack) + len(self.out_stack) == 0


def solution(instructions):
    queue = None

    for i in range(len(instructions[0])):
        instruction, val = instructions[0][i], instructions[1][i]

        if instruction == "MyQueue":
            queue = MyQueue()

        if instruction == "push":
            queue.push(val)

        if instruction == "pop":
            queue.pop()

        if instruction == "peek":
            queue.peek()

        if instruction == "empty":
            queue.empty()
