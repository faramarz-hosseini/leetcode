class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        evens = []
        odds = []

        for num in nums:
            if num % 2 == 0:
                evens.append(num)
            else:
                odds.append(num)

        result = []

        for i in range(len(odds)):
            result.append(evens[i])
            result.append(odds[i])

        return result
