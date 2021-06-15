class Solution:
    def decode(self, encoded: list, first: int) -> list:
        u = [first]

        for j in encoded:
            u.append(j ^ u[-1])
        return u