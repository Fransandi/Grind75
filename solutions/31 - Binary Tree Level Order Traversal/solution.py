"""
Exercise: Binary Tree Level Order Traversal
Difficulty: Medium
Time: 20 min
LeetCode: https://leetcode.com/problems/binary-tree-level-order-traversal/
"""

from helpers import binary_tree


# Time: O(n), Space: O(n), where n is the number of nodes in the binary tree
def solution(root):
    root = binary_tree.array_to_binary_tree(root)

    if not root:
        return []

    level, res = [root], []

    while level:
        res.append([node.val for node in level])
        next_level = []

        while level:
            node = level.pop(0)

            if node.left:
                next_level.append(node.left)
            if node.right:
                next_level.append(node.right)

        level = next_level

    return res
