class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        for i in range(len(nums)):
            count = 0
            for j in range(len(nums)):
                if i == j:
                    continue
                elif nums[i] > nums[j]:
                    count += 1
            result.append(count)

        return result
