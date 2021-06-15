class Solution(object):
    def sortSentence(self, s):
        """
        :type s: str
        :rtype: str
        """
        first = 1
        lst = []
        res = ''
        for word in s.split():
            lst.append((int(word[-1]), word[:-1]))
        for tup in sorted(lst):
            res += tup[1]
            res += ' '
        return res.rstrip()
