class Solution(object):
    def maximum69Number(self, num):
        """
        :type num: int
        :rtype: int
        """
        res = []
        change_allowed = True
        for num in str(num):
            if num != '9' and change_allowed:
                res.append('9')
                change_allowed = False
            else:
                res.append(num)

        return int(''.join(res))
