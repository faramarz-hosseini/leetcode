class Solution(object):
    def halvesAreAlike(self, s):
        """
        :type s: str
        :rtype: bool
        """
        vowels = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
        midpoint = len(s) // 2
        a = s[:midpoint]
        b = s[midpoint:]
        pointer = 0
        a_vowels, b_vowels = 0, 0
        for i in range(midpoint):
            if a[pointer] in vowels:
                a_vowels += 1
            if b[pointer] in vowels:
                b_vowels += 1
            pointer += 1
        if a_vowels == b_vowels:
            return True
        return False
