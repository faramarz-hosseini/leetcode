class Solution(object):
    def isSumEqual(self, firstWord, secondWord, targetWord):
        """
        :type firstWord: str
        :type secondWord: str
        :type targetWord: str
        :rtype: bool
        """
        word_value1, word_value2, word_value3 = '', '', ''

        for i in firstWord:
            word_value1 += str(ord(i) - 97)
        for i in secondWord:
            word_value2 += str(ord(i) - 97)
        for i in targetWord:
            word_value3 += str(ord(i) - 97)
        word_value1, word_value2, word_value3 = int(word_value1), int(word_value2), int(word_value3)

        if word_value1 + word_value2 == word_value3:
            return True
        return False