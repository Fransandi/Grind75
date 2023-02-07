"""
Exercise: Invert Binary Tree
Difficulty: Easy
Time: 15 min
LeetCode: https://leetcode.com/problems/invert-binary-tree/
"""

from helpers import binary_tree


# Time: O(n), Space: O(n), where n is the number of nodes in the binary tree
def solution(nodes):
    root = binary_tree.array_to_binary_tree(nodes)
    root = invert_binary_tree(root)
    return binary_tree.binary_tree_to_array(root)


def invert_binary_tree(root):
    if not root:
        return None

    left, right = root.left, root.right
    root.left = invert_binary_tree(right)
    root.right = invert_binary_tree(left)

    return root
