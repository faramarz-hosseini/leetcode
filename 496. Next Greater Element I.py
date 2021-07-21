class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        for num in nums1:
            nums2_index = nums2.index(num)

            found = False
            for i in range(nums2_index + 1, len(nums2)):
                if nums2[i] > num:
                    found = True
                    result.append(nums2[i])
                    break
            if not found:
                result.append(-1)

        return result