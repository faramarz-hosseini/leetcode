# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        stack = [root]
        d = {}
        node_num = 1
        while stack:
            node = stack.pop()

            if node.val % 2 == 0:
                children = []
                if node.left:
                    children.append(node.left)
                if node.right:
                    children.append(node.right)

                grandchildren = []
                for child in children:
                    if child and child.left:
                        grandchildren.append(child.left.val)
                    if child and child.right:
                        grandchildren.append(child.right.val)

                d[node_num] = sum(grandchildren)
                node_num += 1

            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

        return sum(d.values())
