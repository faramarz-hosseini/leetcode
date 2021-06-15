class Solution(object):
    def balancedStringSplit(self, s):
        """
        :type s: str
        :rtype: int
        """
        rc = 0
        lc = 0
        output = 0

        for char in s:
            if char == "R":
                rc += 1
            elif char == "L":
                lc += 1

            if rc == lc and rc != 0:
                output += 1
                rc, lc = 0, 0

        return output
