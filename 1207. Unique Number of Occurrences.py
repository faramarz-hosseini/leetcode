class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        occurs = {}

        for num in arr:
            if occurs.get(num) is not None:
                occurs[num] += 1
            else:
                occurs[num] = 1

        return len(occurs.values()) == len(set(occurs.values()))
