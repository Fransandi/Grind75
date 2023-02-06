"""
Exercise: Balanced Binary Tree
Difficulty: Easy
Time: 15 min
LeetCode: https://leetcode.com/problems/balanced-binary-tree/
"""

from helpers.binary_tree import array_to_binary_tree


# Time: O(n), Space: O(1), where n is the number of nodes in the binary tree
def solution(root):
    root = array_to_binary_tree(root)
    return is_balanced(root) > 0


def is_balanced(node):
    if node is None:
        return 1

    left, right = is_balanced(node.left), is_balanced(node.right)

    if left < 1 or right < 1 or abs(left - right) > 1:
        return 0

    return max(left, right) + 1
