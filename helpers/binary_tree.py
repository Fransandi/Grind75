class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def build_binary_tree(nodes):
    # Edge case: Tree is empty
    if not nodes:
        return None

    nodes = [None] + [TreeNode(val) for val in nodes]
    for pointer in range(1, len(nodes) + 1):
        left, right = pointer * 2, pointer * 2 + 1
        if left < len(nodes) and nodes[left].val:
            nodes[pointer].left = nodes[left]
        if right < len(nodes) and nodes[right].val:
            nodes[pointer].right = nodes[right]
    return nodes[1]


def tree_to_array(root):
    # Edge case: No root
    if not root:
        return []

    nodes, array = [root], []
    while nodes:
        node = nodes.pop(0)
        array.append(node.val)
        if node.left:
            nodes.append(node.left)
        if node.right:
            nodes.append(node.right)
    return array
