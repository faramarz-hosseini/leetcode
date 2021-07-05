# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        stack = [(root, '')]
        paths = []

        while stack:
            node, path = stack.pop()

            if not node:
                continue

            path += '1'

            stack.append((node.left, path))
            stack.append((node.right, path))

            if not node.left and not node.right:
                paths.append(path)

        longest = 0
        for path in paths:
            if len(path) > longest:
                longest = len(path)

        return longest
