"""
Exercise: 01 Matrix
Difficulty: Medium
Time: 30 min
LeetCode: https://leetcode.com/problems/01-matrix/
"""


# Time: O(n), Space: O(n), where n is the number of cells in the matrix (height * width)
def solution(mat):
    height, width = len(mat), len(mat[0])

    # Intialize the layer with zeros
    layer = set()
    for i, row in enumerate(mat):
        for j, cell in enumerate(row):
            if cell == 0:
                layer.add((i, j))
            else:
                mat[i][j] = None

    # Iterate all layers
    next_val = 1
    while layer:
        next_layer = set()
        for i, j in layer:
            for n_i, n_j in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if (
                    n_i >= 0
                    and n_i < height
                    and n_j >= 0
                    and n_j < width
                    and mat[n_i][n_j] is None
                ):
                    mat[n_i][n_j] = next_val
                    next_layer.add((n_i, n_j))
        layer = next_layer
        next_val += 1

    return mat
