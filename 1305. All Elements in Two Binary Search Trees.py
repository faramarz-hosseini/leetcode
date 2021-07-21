# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        traversals = []
        if root1:
            stack1 = [root1]
            while stack1:
                node = stack1.pop()

                if node.left:
                    stack1.append(node.left)
                if node.right:
                    stack1.append(node.right)
                traversals.append(node.val)
        if root2:
            stack2 = [root2]
            while stack2:
                node = stack2.pop()

                if node.left:
                    stack2.append(node.left)
                if node.right:
                    stack2.append(node.right)
                traversals.append(node.val)

        traversals.sort()
        return traversals