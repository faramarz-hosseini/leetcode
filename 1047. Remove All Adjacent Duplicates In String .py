class Solution:
    def removeDuplicates(self, s: str) -> str:
        while True:
            has_dup, start = self.has_duplicates(s)

            if has_dup == 'YES':
                dup_indexes = self.get_duplicate_indexes(s, start)

                s = s[:dup_indexes[0]] + s[dup_indexes[1] + 1:]

            else:
                break

        return s

    def has_duplicates(self, string: str) -> bool:
        for i in range(len(string) - 1):
            if string[i] == string[i + 1]:
                return ['YES', i]
        return ['NO', -1]

    def get_duplicate_indexes(self, string: str, start: int) -> List[int]:
        for index in range(start, len(string) - 1):
            if string[index] == string[index + 1]:
                return [index, index + 1]
