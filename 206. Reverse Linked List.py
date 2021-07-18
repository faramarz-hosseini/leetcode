# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        previous = None
        following = head
        current = head

        while current:
            following = following.next
            current.next = previous
            previous = current
            current = following

        return previous
