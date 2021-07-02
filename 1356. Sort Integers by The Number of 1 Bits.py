class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        key = 1
        bins = {}

        for num in arr:
            bin_str = bin(num)
            ones = bin_str.count("1")

            if bins.get(ones) is None:
                bins[ones] = [num]
            else:
                bins[ones].append(num)

        result = []
        for key in sorted(bins.keys()):
            for num in sorted(bins[key]):
                result.append(num)

        return result
