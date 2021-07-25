class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d = {}
        d1 = self.count_and_put(nums1)
        d2 = self.count_and_put(nums2)

        for k, v in d1.items():
            if d2.get(k):
                d[k] = v + d2[k]

        res = []
        for k, v in d.items():
            if v > 1:
                res.append(k)

        return res

    def count_and_put(self, arr):
        temp = []
        D = {}
        for num in arr:
            if D.get(num) and num not in temp:
                D[num] += 1
            else:
                D[num] = 1
                temp.append(num)

        return D