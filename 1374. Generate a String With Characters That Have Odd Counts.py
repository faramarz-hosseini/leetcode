class Solution(object):
    def generateTheString(self, n):
        """
        :type n: int
        :rtype: str
        """
        init_result = ''.join([chr(97) for i in range(n - 1)])

        if n % 2 == 0:
            return init_result + 'b'
        else:
            return init_result + 'a'
