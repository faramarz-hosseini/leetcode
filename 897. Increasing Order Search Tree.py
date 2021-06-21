# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        stack = [root]
        traversal = []
        result = None

        while stack:
            node = stack.pop()

            if node:
                traversal.append(node.val)
                stack.append(node.left)
                stack.append(node.right)

        traversal = sorted(traversal)
        nodes = []

        for i in traversal:
            node = TreeNode(i)
            nodes.append(node)

        for i in range(len(nodes) - 1):
            nodes[i].right = nodes[i + 1]
            nodes[i].left = None

        return nodes[0]
