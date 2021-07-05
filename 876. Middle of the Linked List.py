# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        lst = [head]
        vals = []

        while lst:
            node = lst.pop()

            if node:
                vals.append(node)
                lst.append(node.next)

        pointer = len(vals) // 2
        result = vals[pointer]

        return result
