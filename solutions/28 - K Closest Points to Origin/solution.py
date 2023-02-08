"""
Exercise: K Closest Points to Origin
Difficulty: Medium
Time: 30 min
LeetCode: https://leetcode.com/problems/k-closest-points-to-origin/
"""

import heapq
import random


# Solution 1: Sorting -> Time: O(n log n), Space: O(1), where n is the length of the points array
def solution(points, k):
    return sorted(points, key=distance_to_origin)[:k]


# Solution 2: Heap -> Time: O(n log k), Space: O(k), where n is the length of the points array
def solution2(points, k):
    heap = []

    for point in points:
        el = (-distance_to_origin(point), point[0], point[1])

        if len(heap) == k:
            heapq.heappushpop(heap, el)
        else:
            heapq.heappush(heap, el)

    return sorted([[x, y] for _, x, y in heap], reverse=True)


# Solution 3: Quick Select -> Time O(n) <Wors caste: O(n2)>, Space -> O(1), where n is the length of the points array
def solution3(points, k):
    distances = [(distance_to_origin(point), point) for point in points]

    def partition(l, r):
        pivot_index = random.randint(l, r)  # Randomly select pivot
        pivot_distance = distances[pivot_index][0]

        distances[pivot_index], distances[r] = distances[r], distances[pivot_index]

        store_index = l
        for i in range(l, r):
            if distances[i][0] < pivot_distance:
                distances[store_index], distances[i] = (
                    distances[i],
                    distances[store_index],
                )
                store_index += 1

        distances[store_index], distances[r] = distances[r], distances[store_index]
        return store_index

    def quickselect(l, r, k):
        if l < r:
            index = partition(l, r)

            if index == k:
                return
            elif index < k:
                quickselect(index + 1, r, k)
            else:
                quickselect(l, index - 1, k)

    quickselect(0, len(points) - 1, k)
    return [point for _, point in distances[:k]]


# Helper functions
def distance_to_origin(point):
    return pow(point[0], 2) + pow(point[1], 2)
