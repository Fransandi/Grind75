"""
Exercise: Number of Islands
Difficulty: Medium
Time: 25 min
LeetCode: https://leetcode.com/problems/number-of-islands/
"""


# Time: O(n), Space: O(1), where n is the number of land cells in the grid
def solution(grid):
    islands = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "1":
                clean_island(grid, i, j)
                islands += 1

    return islands


def clean_island(grid, i, j):
    if grid[i][j] == "1":
        grid[i][j] = "0"

        if i > 0:
            clean_island(grid, i - 1, j)
        if i < len(grid) - 1:
            clean_island(grid, i + 1, j)
        if j > 0:
            clean_island(grid, i, j - 1)
        if j < len(grid[0]) - 1:
            clean_island(grid, i, j + 1)
