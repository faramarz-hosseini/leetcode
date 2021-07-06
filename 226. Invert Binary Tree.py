# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        first = root
        queue = [root]

        while queue:
            node = queue.pop(0)

            if node:
                temp = node.left
                node.left = node.right
                node.right = temp

                queue.append(node.left)
                queue.append(node.right)

        return first
