class Solution(object):
    def countConsistentStrings(self, allowed, words):
        """
        :type allowed: str
        :type words: List[str]
        :rtype: int
        """
        c = 0
        for word in words:
            for letter in word:
                if letter not in allowed:
                    c -= 1
                    break
            c += 1
        if c < 0:
            c = 0

        return c
