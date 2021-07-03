class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        lucky_nums = []
        cols = self.make_columns(matrix)

        for row in matrix:
            for number in row:
                col = self.find_col(number, cols)
                is_lucky = self.is_lucky(number, row, col)

                if is_lucky:
                    lucky_nums.append(number)

        return lucky_nums

    def make_columns(self, matrix):
        cols_count = len(matrix[0])
        cols = []

        for num in range(cols_count):
            cols.append([])

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                cols[j].append(matrix[i][j])

        return cols

    def find_col(self, number, columns):
        for col in columns:
            if number in col:
                return col
        return None

    def is_lucky(self, number, row, column):
        if max(column) == number and min(row) == number:
            return True
        return False
