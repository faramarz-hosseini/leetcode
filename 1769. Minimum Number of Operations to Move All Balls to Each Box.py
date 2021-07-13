class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        result = []
        for i in range(len(boxes)):
            ops = 0
            for j in range(len(boxes)):
                if i != j and boxes[j] == '1':
                    ops += abs(i - j)
            result.append(ops)

        return result
