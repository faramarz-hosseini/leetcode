# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        stack = [root]

        org_vals = []
        while stack:
            node = stack.pop()

            org_vals.append(node.val)

            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

        new_vals = []
        for i in range(len(org_vals)):
            org = org_vals[i]
            current = org_vals[i]
            for j in range(len(org_vals)):
                if i != j and org_vals[j] > org_vals[i]:
                    current += org_vals[j]
            new_vals.append((org, current))

        stack = [root]
        pointer = 0
        while stack:
            node = stack.pop()

            node.val = new_vals[pointer][1]
            pointer += 1

            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

        return root
