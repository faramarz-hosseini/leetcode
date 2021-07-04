"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def maxDepth(self, root: 'Node') -> int:
        stack = [(root, '')]
        traversals = []
        count = 0

        while stack:
            node, path = stack.pop()

            if node:
                path += '1'

                if not node.children:
                    traversals.append(path)
                    continue

                for node in node.children:
                    stack.append((node, path))

        longest_path = 0
        for path in traversals:
            if len(path) > longest_path:
                longest_path = len(path)

        return longest_path
