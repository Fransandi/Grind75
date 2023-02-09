"""
Exercise: Validate Binary Search Tree
Difficulty: Medium
Time: 20 min
LeetCode: https://leetcode.com/problems/validate-binary-search-tree/
"""

from helpers import binary_tree


# Exploring Tree -> Time: O(n), Space: O(1), where n is the number of nodes in the binary tree
def solutiona(root):
    root = binary_tree.array_to_binary_tree(root)

    def helper(root, min_val, max_val):
        if root is None:
            return True

        if root.val < min_val or root.val > max_val:
            return False

        return helper(root.left, min_val, root.val - 1) and helper(
            root.right, root.val + 1, max_val
        )

    return helper(root, float("-inf"), float("inf"))


# Inorder -> Time: O(n), Space: O(1), where n is the number of nodes in the binary tree
def solution(root):
    root = binary_tree.array_to_binary_tree(root)

    def inorder(root):
        if not root:
            return []

        return inorder(root.left) + [root.val] + inorder(root.right)

    inorder_list = inorder(root)

    # Check if items are repeated
    if len(inorder_list) != len(set(inorder_list)):
        return False

    return inorder_list == sorted(inorder_list)
