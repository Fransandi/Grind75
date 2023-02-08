"""
Exercise: Clone Graph
Difficulty: Medium
Time: 25 min
LeetCode: https://leetcode.com/problems/clone-graph/
"""

from helpers import graph


# Time: O(), Space: O()
def solution(adjList):
    node = graph.adj_list_to_graph(adjList)

    if not node:
        return node

    queue = [node]
    clones = {node.val: graph.Node(node.val, [])}

    while queue:
        cur = queue.pop(0)
        cur_clone = clones[cur.val]

        for ngbr in cur.neighbors:
            if ngbr.val not in clones:
                clones[ngbr.val] = graph.Node(ngbr.val, [])
                queue.append(ngbr)

            cur_clone.neighbors.append(clones[ngbr.val])

    return graph.graph_to_adj_list(clones[node.val])
