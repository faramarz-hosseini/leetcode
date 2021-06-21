class Solution(object):
    def sortArrayByParity(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        odds, evens = [], []

        for i in nums:
            if i % 2 == 0:
                evens.append(i)
            else:
                odds.append(i)

        return evens + odds
