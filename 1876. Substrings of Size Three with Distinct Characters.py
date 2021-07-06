class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        good_subs = 0

        pointer = 0
        for i in range(len(s) - 2):
            sub = s[pointer:pointer + 3]
            print(sub)
            if len(list(sub)) == len(set(sub)):
                good_subs += 1

            pointer += 1

        return good_subs
