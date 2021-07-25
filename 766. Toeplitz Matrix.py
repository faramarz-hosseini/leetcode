class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        for i in range(len(matrix) - 1): # We don't need to check the last row.
            for j in range(len(matrix[i])):
                if j < len(matrix[i]) - 1 and matrix[i][j] != matrix[i + 1][j + 1]:
                    return False
        return True
