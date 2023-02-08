"""
Graph Helper
Collection of classes/methods to help define and parse the input/output expected from LeetCode
"""


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


def adj_list_to_graph(adjList):
    nodes = {1: Node()}

    for i in range(len(adjList)):
        nodes[i + 1] = Node(i + 1)

    for i in range(len(adjList)):
        ngbrs = adjList[i]

        for ngbr in ngbrs:
            nodes[i + 1].neighbors.append(nodes[ngbr])

    return nodes[1] if 1 in nodes else Node()


def graph_to_adj_list(node):
    nodes = {}
    queue = [node]
    while queue:
        cur = queue.pop(0)
        nodes[cur.val] = [n.val for n in cur.neighbors]

        for ngbr in cur.neighbors:
            if ngbr.val not in nodes:
                queue.append(ngbr)

    sol = []
    for i in range(1, max(nodes.keys()) + 1):
        sol.append(nodes[i] if i in nodes else [])
    return sol
