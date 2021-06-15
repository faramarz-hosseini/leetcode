class Solution(object):
    def countGoodRectangles(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: int
        """
        lengths = []
        for rect in rectangles:
            lengths.append(min(rect))
        maxLen = max(lengths)
        return lengths.count(maxLen)
