'''
Exercise: Flood Fill
Difficulty: Easy
Time: 20 min
LeetCode: https://leetcode.com/problems/flood-fill/
'''


def solution(image, sr, sc, color):
    initial_color = image[sr][sc]

    # Edge case: the first cell is already from the final color
    if color == initial_color:
        return image

    return fill(image, sr, sc, color, initial_color)

def fill(image, sr, sc, color, initial_color):

    if image[sr][sc] == initial_color:
        image[sr][sc] = color

        for (r, c) in get_neighbours(image, sr, sc):
            fill(image, r, c, color, initial_color)

    return image

def get_neighbours(image, sr, sc):
    return [(r, c) for (r, c) in [(sr+1, sc), (sr-1, sc), (sr, sc+1), (sr, sc-1)] if r >= 0 and r < len(image[0]) and c >= 0 and c < len(image)]
