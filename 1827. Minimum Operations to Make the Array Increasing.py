class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        operations = 0
        if len(nums) < 2:
            return operations

        for i in range(0, len(nums) - 1):
            if nums[i + 1] == nums[i]:
                operations += 1
                nums[i + 1] = nums[i] + 1

            elif nums[i + 1] < nums[i]:
                operations += (nums[i] - nums[i + 1]) + 1
                nums[i + 1] = nums[i] + 1

        print(nums)
        return operations
