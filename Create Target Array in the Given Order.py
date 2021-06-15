class Solution(object):
    def createTargetArray(self, nums, index):
        """
        :type nums: List[int]
        :type index: List[int]
        :rtype: List[int]
        """
        target = []
        i = 0
        for _ in range(len(nums)):
            target.insert(index[i], nums[i])
            i += 1

        return target
