class Solution(object):
    def checkIfPangram(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """
        letters = {}
        for letter in sentence:
            if letters.get(letter):
                letters[letter] += 1
            else:
                letters[letter] = 0
        if len(letters) == 26:
            return True
        return False