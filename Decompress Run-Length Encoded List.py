class Solution(object):
    def decompressRLElist(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        for i in range(0, len(nums), 2):
            lst = []
            length = nums[i]
            val = nums[i+1]
            for i in range(length):
                lst.append(val)
            res.append(lst)
        result = []
        for lst in res:
            result += lst
        return result