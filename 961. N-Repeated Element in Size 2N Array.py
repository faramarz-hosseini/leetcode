class Solution(object):
    def repeatedNTimes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Make a dictionary of numbers with their counts as the value
        numbers = {}

        # Create, increment and at the same time check if a key has a value more than 1. If so return
        for num in nums:
            if numbers.get(num):
                numbers[num] += 1
            else:
                numbers[num] = 1

            if numbers.get(num) > 1:
                return num
