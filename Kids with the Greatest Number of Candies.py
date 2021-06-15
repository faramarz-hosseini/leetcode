class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        res = []
        max_candies = max(candies)
        for candy in candies:
            if candy + extraCandies >= max_candies:
                res.append(True)
            else:
                res.append(False)
        return res
