class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        final_sentence = ""
        vowels = ["a", "e", "i", "o", "u"]
        vowels = [letter.upper() for letter in vowels] + vowels
        words = sentence.split()
        number_of_a = 1

        for word in words:
            if word[0] in vowels:
                new_word = word + "ma"

                for a in range(number_of_a):
                    new_word += "a"

                final_sentence += new_word + " "

            else:
                new_word = word[1:] + word[0] + "ma"

                for a in range(number_of_a):
                    new_word += "a"

                final_sentence += new_word + " "

            number_of_a += 1

        return final_sentence.rstrip()
