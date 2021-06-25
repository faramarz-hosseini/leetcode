class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        # -1 because we do not want to modify the last element in our loop.
        indexes = len(arr) - 1

        for index in range(indexes):
            arr[index] = max(arr[index + 1:])

        # A single operation to modify the last element.
        arr[-1] = -1

        return arr
