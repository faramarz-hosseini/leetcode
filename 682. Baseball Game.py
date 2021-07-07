class COMMANDS:
    CM = {'double': "D", 'invalidate': 'C', 'plus': '+'}


class Solution:
    def calPoints(self, ops: List[str]) -> int:
        records = []

        for op in ops:
            if op not in COMMANDS.CM.values():
                records.append(int(op))
                continue

            if COMMANDS.CM['double'] == op:
                records.append(records[-1] * 2)
            elif COMMANDS.CM['invalidate'] == op:
                records.pop()
            else:
                records.append(records[-1] + records[-2])

        return sum(records)
