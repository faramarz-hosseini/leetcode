class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        word1, word2 = list(word1), list(word2)

        result = ''

        while word1 and word2:
            result += word1.pop(0)
            result += word2.pop(0)

        if word1:
            result += ''.join(word1)
        if word2:
            result += ''.join(word2)

        return result
