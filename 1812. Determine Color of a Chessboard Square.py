class Solution(object):
    b, a = 'black', 'white'
    INFO = {'a': b, 'b': a, 'c': b, 'd': a, 'e': b, 'f': a, 'g': b, 'h': a}

    def switch(self, color):
        colors = ['black', 'white']

        if color == colors[0]:
            return colors[1]
        elif color == colors[1]:
            return colors[0]

    def squareIsWhite(self, coordinates):
        """
        :type coordinates: str
        :rtype: bool
        """
        column, row = coordinates
        color = Solution.INFO[column]

        for i in range(1, int(row)):
            color = self.switch(color)

        if color == 'white':
            return True
        return False