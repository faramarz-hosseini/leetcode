class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        extra_list = []

        for num in arr1:
            if num not in arr2:
                extra_list.append(num)

        extra_list.sort()

        result = []
        for num in arr2:
            result = self.rel_sort(num, arr1, result)

        return result + extra_list

    def rel_sort(self, target, arr, result):
        for num in arr:
            if num == target:
                result.append(num)
        return result