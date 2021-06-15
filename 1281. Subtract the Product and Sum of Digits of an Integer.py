class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        n = str(n)
        p_ans, s_ans = 1, 0
        for i in range(0,len(n)):
            p_ans *= int(n[i])
            s_ans += int(n[i])
        return p_ans - s_ans
