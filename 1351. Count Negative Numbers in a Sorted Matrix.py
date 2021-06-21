class Solution(object):
    def countNegatives(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        output = 0

        for row in grid:
            for num in reversed(row):
                if num >= 0:
                    break
                output += 1

        return output
