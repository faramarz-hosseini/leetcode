class Solution(object):
    def numberOfMatches(self, n):
        """
        :type n: int
        :rtype: int
        """
        matches = 0
        teams = n
        while teams != 1:
            match = teams // 2
            matches += match
            teams -= match
        return matches
