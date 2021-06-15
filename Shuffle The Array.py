class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        output = []
        for i in range(n):
            output.append(nums[i])
            output.append(nums[i + n])
        return output
