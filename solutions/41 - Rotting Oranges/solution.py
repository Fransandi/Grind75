"""
Exercise: Rotting Oranges
Difficulty: Medium
Time: 30 min
LeetCode: https://leetcode.com/problems/rotting-oranges/
"""


# Time: O(n), Space: O(n), where n is the total amount of cells.
def solution(grid):
    rotten, fresh, minutes = [], 0, 0

    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell == 2:
                rotten.append((i, j))
            if cell == 1:
                fresh += 1

    while rotten:
        next_layer = []
        for i, j in rotten:
            for n_i, n_j in get_neighbours(grid, i, j):
                if grid[n_i][n_j] == 1:
                    grid[n_i][n_j] = 2
                    fresh -= 1
                    next_layer.append((n_i, n_j))

        rotten = next_layer

        if rotten:
            minutes += 1

    if fresh:
        return -1

    return minutes


def get_neighbours(grid, i, j):
    return [
        (n_i, n_j)
        for (n_i, n_j) in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]
        if n_i >= 0 and n_i < len(grid) and n_j >= 0 and n_j < len(grid[0])
    ]
