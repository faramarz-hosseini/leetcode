class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        users = {}

        for log in logs:
            if users.get(log[0]):
                users[log[0]].add(log[1])
            else:
                users[log[0]] = {log[1]}

        result = [0 for i in range(k)]

        for key in users:
            uam = len(users[key])
            result[uam - 1] += 1

        return result
