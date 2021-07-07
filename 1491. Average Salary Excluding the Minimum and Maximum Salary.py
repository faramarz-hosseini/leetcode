class Solution:
    def average(self, salary: List[int]) -> float:
        divisor = len(salary) - 2

        minimum, maximum = float("+inf"), float("-inf")
        for num in salary:
            if num > maximum:
                maximum = num
            if num < minimum:
                minimum = num

        summ = 0
        for num in salary:
            if num != maximum and num != minimum:
                summ += num

        return summ / divisor
