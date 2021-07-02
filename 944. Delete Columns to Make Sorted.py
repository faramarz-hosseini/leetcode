class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        alph = ''.join([chr(num) for num in range(97, 123)])
        deleted = 0

        cols = self.make_columns(strs)
        for col in cols:
            is_sorted = self.is_sorted(col, alph)

            if not is_sorted:
                deleted += 1

        return deleted

    def make_columns(self, arr: List[str]) -> List[str]:
        columns_count = len(arr)
        strings_len = len(arr[0])  # Strings are of same length.
        cols = []
        pointer = 0

        for j in range(strings_len):
            col = []
            for i in range(columns_count):
                col.append(arr[i][pointer])
            pointer += 1
            cols.append(col)

        return cols

    def is_sorted(self, col, compare):

        for index in range(len(col) - 1):
            if compare.find(col[index]) > compare.find(col[index + 1]):
                return False
            else:
                continue

        return True
