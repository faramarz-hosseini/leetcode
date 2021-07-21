class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}

        for i in range(len(nums)):
            compliment = target - nums[i]

            if d.get(compliment) is not None:
                return [i, d[compliment]]
            else:
                d[nums[i]] = i