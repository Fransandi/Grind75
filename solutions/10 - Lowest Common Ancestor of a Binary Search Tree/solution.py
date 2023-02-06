"""
Exercise: Lowest Common Ancestor of a Binary Search Tree
Difficulty: Easy
Time: 20 min
LeetCode: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
"""

from helpers.binary_tree import array_to_binary_tree


# Time: O(h), Space: O(1), where h is the height of the binary tree
def solution(root, p, q):
    root = array_to_binary_tree(root)

    while root:
        if root.val > max(p, q):
            root = root.left
        elif root.val < min(p, q):
            root = root.right
        else:
            return root.val
    return None
