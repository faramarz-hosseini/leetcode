# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        stack = [(root, "")]
        paths = []

        while stack:
            node, path = stack.pop()

            if node:
                path += str(node.val)

                if node.right:
                    stack.append((node.right, path))
                if node.left:
                    stack.append((node.left, path))

                if node.right is None and node.left is None:
                    paths.append(path)

        result = 0
        for path in paths:
            result += int(path, 2)

        return result
+