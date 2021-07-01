class Solution:
    def countBits(self, n: int) -> List[int]:
        result = []

        for i in range(n + 1):
            ones = self.count_ones_in_bin(i)
            result.append(ones)

        return result

    def count_ones_in_bin(self, number):
        count = 0
        for num in bin(number):
            if num == '1':
                count += 1

        return count