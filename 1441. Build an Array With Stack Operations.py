class COMMANDS:
    PUSH = 'Push'
    POP = 'Pop'


class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        result = []
        compare_list = []

        for i in range(1, n + 1):
            if compare_list == target:
                break

            if i in target:
                result.append(COMMANDS.PUSH)
                compare_list.append(i)
            else:
                result.append(COMMANDS.PUSH)
                result.append(COMMANDS.POP)

        return result
