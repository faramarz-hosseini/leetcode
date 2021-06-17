class Solution(object):
    def busyStudent(self, startTime, endTime, queryTime):
        """
        :type startTime: List[int]
        :type endTime: List[int]
        :type queryTime: int
        :rtype: int
        """
        output = 0

        for i in range(len(endTime)):
            if startTime[i] <= queryTime <= endTime[i]:
                output += 1

        return output
