class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        keyboard = {1: "qwertyuiop", 2: "asdfghjkl", 3: "zxcvbnm"}

        result = []
        row = 0
        for word in words:
            letter = word[0]
            if letter in keyboard[1] or letter.lower() in keyboard[1]:
                row = 1
            elif letter in keyboard[2] or letter.lower() in keyboard[2]:
                row = 2
            else:
                row = 3

            can_be_typed = True
            for letter in word[1:]:
                if letter not in keyboard[row] and letter.lower() not in keyboard[row]:
                    can_be_typed = False
                    break
            if can_be_typed:
                result.append(word)

        return result
