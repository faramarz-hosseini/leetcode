# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        _sum = 0
        stack = [(root, '')]
        paths = []

        while stack:
            node, path = stack.pop()

            path += str(node.val) + ','
            if node.left:
                stack.append((node.left, path))
            if node.right:
                stack.append((node.right, path))

            if not node.left and not node.right:
                paths.append(path)

        paths = [s.split(',') for s in paths]
        deepest_len = 0
        for path in paths:
            if len(path) > deepest_len:
                deepest_len = len(path)

        for path in paths:
            if len(path) == deepest_len:
                _sum += int(path[-2])

        return _sum
