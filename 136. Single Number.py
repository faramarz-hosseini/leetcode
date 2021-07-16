class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        info = {}

        for i in range(len(nums)):
            if info.get(nums[i]):
                info[nums[i]] += 1
            else:
                info[nums[i]] = 1

        for k, v in info.items():
            if v == 1:
                return k

