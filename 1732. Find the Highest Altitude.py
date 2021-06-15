class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        highest = 0
        start = 0
        for g in gain:
            start += g
            if start > highest:
                highest = start
        return highest
