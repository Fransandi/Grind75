"""
Exercise: Course Schedule
Difficulty: Medium
Time: 30 min
LeetCode: https://leetcode.com/problems/course-schedule/
"""


# Time: O(v + e), Space: O(v + e), where v is the number of vertices and e is the number edges in the graph
def solution(numCourses, prerequisites):
    states = [0] * numCourses
    adjacency_list = [[] for _ in range(numCourses)]
    for course, pre in prerequisites:
        adjacency_list[course].append(pre)

    def hasCycle(v):
        # Vertex was already processed
        if states[v] == 2:
            return False

        # Vertex is being processed, cycle found
        if states[v] == 1:
            return True

        # Start processing vertex
        states[v] = 1
        for adj_v in adjacency_list[v]:
            if hasCycle(adj_v):
                return True

        # Vertex finished being processed
        states[v] = 2
        return False

    for course in range(numCourses):
        if hasCycle(course):
            return False
    return True
