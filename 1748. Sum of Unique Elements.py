class Solution(object):
    def sumOfUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_count = {}
        result = 0

        for num in nums:
            if nums_count.get(num) is None:
                nums_count[num] = 1
            else:
                nums_count[num] += 1

        for number, count in nums_count.items():
            if count == 1:
                result += number

        return result
