class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        max_wealth = 0
        for person in accounts:
            wealth = sum(person)
            if wealth > max_wealth:
                max_wealth = wealth
        return max_wealth