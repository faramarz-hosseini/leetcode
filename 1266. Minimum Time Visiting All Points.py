class Solution:
    def minTimeToVisitAllPoints(self, points):
        count = 0
        # begin from the 1st point and set it as the current point
        x0, y0 = points[0]
        for point in points[1:]:
            x, y = point
            n = max(abs(x-x0), abs(y-y0))
            count += n
            # replace the current point with next point
            x0, y0 = x, y
        return count

