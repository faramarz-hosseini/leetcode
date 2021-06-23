"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        stack = [root]
        dfs_traversal = []

        while stack:
            node = stack.pop()
            if node:
                for child in reversed(node.children):
                    stack.append(child)
                dfs_traversal.append(node.val)

        return dfs_traversal
