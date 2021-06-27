class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = sorted(heights)
        expected_indexes = len(expected) - 1
        anomalies = 0

        for index in range(expected_indexes + 1):
            if expected[index] != heights[index]:
                anomalies += 1
            else:
                continue

        return anomalies
