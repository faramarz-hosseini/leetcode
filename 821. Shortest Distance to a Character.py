class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        c_indexes = []

        for index in range(len(s)):
            if s[index] == c:
                c_indexes.append(index)

        result = []
        for index in range(len(s)):
            ans = self.find_closest_target(c_indexes, index)
            result.append(ans)

        return result

    def find_closest_target(self, target_inds, current_index):
        possible_answers = []

        for ind in target_inds:
            absolute = abs(ind - current_index)
            possible_answers.append(absolute)

        return min(possible_answers)
