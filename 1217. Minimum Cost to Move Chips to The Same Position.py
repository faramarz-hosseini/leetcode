class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        dom = self.find_dominant(position)

        cost = 0
        if dom == 'evens':
            for pos in position:
                if pos % 2 != 0:
                    cost += 1

        else:
            for pos in position:
                if pos % 2 == 0:
                    cost += 1

        return cost

    def find_dominant(self, arr: List[int]) -> str:
        odds, evens = 0, 0

        for num in arr:
            if num % 2 == 0:
                evens += 1
            elif num % 2 != 0:
                odds += 1

        return "odds" if odds > evens else "evens"
