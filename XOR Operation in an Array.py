class Solution(object):
    def xorOperation(self, n, start):
        """
        :type n: int
        :type start: int
        :rtype: int
        """
        output = start
        nums = []
        for i in range(n):
            num = start + 2 * i
            nums.append(num)
        for num in nums[1:]:
            output = output ^ num
        return output
