class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        while s.find(part) >= 0:
            cut_start = s.find(part)
            cut_end = len(part)
            s = s[:cut_start] + s[cut_start+cut_end:]
        return s
