class Solution(object):
    UP = 'U'
    DOWN = 'D'
    LEFT = 'L'
    RIGHT = 'R'

    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        x_coordinate = 0
        y_coordinate = 0

        for move in moves:
            if move == self.UP:
                x_coordinate += 1
            elif move == self.DOWN:
                x_coordinate -= 1

            elif move == self.RIGHT:
                y_coordinate += 1
            elif move == self.LEFT:
                y_coordinate -= 1

        if x_coordinate == 0 and y_coordinate == 0:
            return True
        return False
