"""
Exercise: Invert Binary Tree
Difficulty: Easy
Time: 15 min
LeetCode: https://leetcode.com/problems/invert-binary-tree/
"""

from helpers.binary_tree import build_binary_tree, tree_to_array


def solution(nodes):
    root = build_binary_tree(nodes)
    root = invert_tree(root)
    return tree_to_array(root)


def invert_tree(root):
    if not root:
        return None

    left, right = root.left, root.right
    root.left = invert_tree(right)
    root.right = invert_tree(left)

    return root
