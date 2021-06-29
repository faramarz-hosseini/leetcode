class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums

        nums = sorted(nums)[::-1]
        pointer = 1

        result = [nums[0]]
        while sum(result) <= sum(nums[pointer:]):
            pointer += 1
            result = nums[:pointer]

        return result
