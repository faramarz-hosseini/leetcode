# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:

        queue = [root]

        while queue:
            node = queue.pop(0)

            if node:
                if node.val > val:
                    queue.append(node.left)
                elif node.val < val:
                    queue.append(node.right)
                else:
                    return node
