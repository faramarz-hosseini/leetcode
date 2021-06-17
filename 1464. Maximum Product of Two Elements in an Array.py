class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        max_product = 0

        for i in range(len(nums)):
            for j in range(len(nums)):
                if i == j:
                    continue
                else:
                    new_max = (nums[i] - 1) * (nums[j] - 1)
                    if new_max > max_product:
                        max_product = new_max

        return max_product
