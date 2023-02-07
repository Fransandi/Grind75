"""
Exercise: Maximum Depth of Binary Tree
Difficulty: Easy
Time: 15 min
LeetCode: https://leetcode.com/problems/maximum-depth-of-binary-tree/
"""

from helpers import binary_tree


# Time: O(n), Space: O(n), where n is the number of nodes in the binary tree
def solution(root):
    root = binary_tree.array_to_binary_tree(root)
    return calculate_depth(root)


def calculate_depth(root):
    # Base case: reached lowest level
    if root is None:
        return 0

    return 1 + max(calculate_depth(root.left), calculate_depth(root.right))
