class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        lengths = 0
        info = {}

        for char in chars:
            if info.get(char):
                info[char] += 1
            else:
                info[char] = 1

        vals = [val for val in info.values()]
        for word in words:
            flag = True

            for letter in word:
                if info.get(letter) == 0 or info.get(letter) is None:
                    flag = False
                    break
                else:
                    info[letter] -= 1

            if flag:
                lengths += len(word)

            pointer = 0
            for key in info:
                info[key] = vals[pointer]
                pointer += 1

        return lengths
