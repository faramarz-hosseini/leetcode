class Solution:
    def is_valid(self, lst):
        last = -1
        for num in lst:
            if num > last:
                last = num
            else:
                return False
        return True

    def canBeIncreasing(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        possibility = []

        for i in range(len(nums)):
            new_nums = nums.copy()
            new_nums.pop(i)
            possibility.append(self.is_valid(new_nums))

        print(possibility)
        if True in possibility:
            return True
        return False
    