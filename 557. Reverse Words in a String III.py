class Solution:
    def reverseWords(self, s: str) -> str:
        string_words = s.split()
        res = ''

        for word in string_words:
            res += word[::-1]
            res += ' '

        return res.rstrip()
