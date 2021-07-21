# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        s1, s2 = "", ""
        while l1 is not None:
            s1 += str(l1.val)
            l1 = l1.next
        while l2 is not None:
            s2 += str(l2.val)
            l2 = l2.next

        s1 = s1[::-1]
        s2 = s2[::-1]
        ans = int(s1) + int(s2)

        ans_sol = str(ans)[::-1]

        result_nodes = []
        for num in ans_sol:
            result_nodes.append(ListNode(int(num)))

        for i in range(len(result_nodes) - 1):
            result_nodes[i].next = result_nodes[i + 1]

        return result_nodes[0]