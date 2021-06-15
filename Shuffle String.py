class Solution(object):
    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
        res = {}
        result = ''
        for i in range(len(s)):
            res[indices[i]] = s[i]
        for i in range(len(res)):
            minimum = min(res)
            result += res[minimum]
            del res[minimum]
        return result

