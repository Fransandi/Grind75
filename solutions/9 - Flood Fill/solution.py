"""
Exercise: Flood Fill
Difficulty: Easy
Time: 20 min
LeetCode: https://leetcode.com/problems/flood-fill/
"""


# Time: O(n), Space: O(n), where n is the number of cells in the image matrix
def solution(image, sr, sc, color):
    initial_color = image[sr][sc]

    # Edge case: the first cell is already from the final color
    if color == initial_color:
        return image

    return fill(image, sr, sc, color, initial_color)


def fill(image, sr, sc, color, initial_color):
    if image[sr][sc] == initial_color:
        image[sr][sc] = color

        for r, c in get_neighbours(image, sr, sc):
            fill(image, r, c, color, initial_color)

    return image


def get_neighbours(image, r, c):
    height, width = len(image[0]), len(image)
    return [
        (n_r, n_c)
        for (n_r, n_c) in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]
        if n_r >= 0 and n_r < height and n_c >= 0 and n_c < width
    ]
