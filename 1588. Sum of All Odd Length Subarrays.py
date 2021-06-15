class Solution(object):
    def sumOddLengthSubarrays(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        starting_sum = sum(arr)
        end_index = len(arr)
        pointer1, pointer2 = 0, 0
        subarr_lengths = [i for i in range(3, len(arr) + 1) if i % 2 != 0]
        sub_arrays = []

        for subarr_length in subarr_lengths:
            pointer2 = subarr_length - 1
            while pointer2 < end_index:
                sub_arrays.append(arr[pointer1:pointer2 + 1])
                pointer1 += 1
                pointer2 += 1
            pointer1, pointer2 = 0, 0
        for arr in sub_arrays:
            starting_sum += sum(arr)

        return starting_sum