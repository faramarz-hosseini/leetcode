class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        indices = []
        index = 0

        for row in mat:
            indices.append([row, index])
            index += 1

        indices.sort()

        result = []

        for i in range(k):
            res = indices.pop(0)[1]

            result.append(res)

        return result
