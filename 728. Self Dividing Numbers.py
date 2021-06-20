class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        result = []

        for num in range(left, right + 1):
            divis = True

            for i in str(num):
                if int(i) == 0:
                    divis = False
                    break
                if num % int(i) != 0:
                    divis = False
                    break

            if divis:
                result.append(num)

        return result
