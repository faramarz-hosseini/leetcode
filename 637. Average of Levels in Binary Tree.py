# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        queue = [root]

        level_sum = 0
        res = []
        while queue:
            level_sum = 0

            level_size = len(queue)

            for i in range(level_size):
                node = queue.pop(0)
                level_sum += node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            res.append(level_sum / level_size)

        return res
