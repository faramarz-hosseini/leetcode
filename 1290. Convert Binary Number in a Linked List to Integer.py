class Solution(object):
    def getDecimalValue(self, head):
        """
        :type head: ListNode
        :rtype: int
        """
        res = ''
        current = head
        power = 0
        output = 0

        while current:
            res += str(current.val)
            current = current.next
        for num in res[::-1]:
            if int(num) == 1:
                output += 2 ** power
            power += 1
        return output