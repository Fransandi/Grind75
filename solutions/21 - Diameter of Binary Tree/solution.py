"""
Exercise: Diameter of Binary Tree
Difficulty: Easy
Time: 30 min
LeetCode: https://leetcode.com/problems/diameter-of-binary-tree/
"""

from helpers import binary_tree


# Time: O(n), Space: O(n), where n is the number of nodes in the binary tree
def solution(root):
    root = binary_tree.array_to_binary_tree(root)
    max_diameter = 0

    def calculate_max_diameter(root):
        if root is None:
            return 0

        left = calculate_max_diameter(root.left)
        right = calculate_max_diameter(root.right)

        nonlocal max_diameter
        max_diameter = max(max_diameter, left + right)

        return max(left, right) + 1

    calculate_max_diameter(root)
    return max_diameter
