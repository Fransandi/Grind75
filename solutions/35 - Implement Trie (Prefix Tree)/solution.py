"""
Exercise: Implement Trie (Prefix Tree)
Difficulty: Medium
Time: 35 min
LeetCode: https://leetcode.com/problems/implement-trie-prefix-tree/
"""


class Trie:
    def __init__(self):
        self.root = {}

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node:
                node[char] = {}
            node = node[char]
        node["."] = True

    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if char not in node:
                return False
            node = node[char]
        return "." in node

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            if char not in node:
                return False
            node = node[char]
        return True


# Time: O(n), Space: O(n), where n is the length of the word/prefix strings in the operations
def solution(instructions):
    trie, result = None, []
    for i in range(len(instructions[0])):
        instruction, val = instructions[0][i], instructions[1][i]
        res = None

        if instruction == "Trie":
            trie = Trie()
        if instruction == "insert":
            res = trie.insert(val)
        if instruction == "search":
            res = trie.search(val)
        if instruction == "startsWith":
            res = trie.startsWith(val)

        result.append(res)

    return result
