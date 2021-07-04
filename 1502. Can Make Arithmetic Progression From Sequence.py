class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        if len(arr) == 2:
            return True

        arr.sort()
        diff = arr[0] - arr[1]
        for ind in range(1, len(arr) - 1):
            new_diff = arr[ind] - arr[ind + 1]
            if new_diff != diff:
                return False
            else:
                diff = new_diff

        return True
