class Solution(object):
    def convert_ballnum_to_box(self, ball_num):
        box_number = 0
        for num in [int(num) for num in str(ball_num)]:
            box_number += num

        return box_number

    def countBalls(self, lowLimit, highLimit):
        """
        :type lowLimit: int
        :type highLimit: int
        :rtype: int
        """
        balls = {}

        for ball_num in range(lowLimit, highLimit + 1):
            box_num = self.convert_ballnum_to_box(ball_num)

            if balls.get(box_num) is not None:
                balls[box_num] += 1
            else:
                balls[box_num] = 1

        return max(balls.values())
