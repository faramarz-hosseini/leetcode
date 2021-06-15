class Solution(object):
    def destCity(self, paths):
        """
        :type paths: List[List[str]]
        :rtype: str
        """
        p = {}

        for path in paths:
            p[path[0]] = path[1]

        for path in paths:
            city1, city2 = path

            if city1 not in p.keys():
                return city1
            elif city2 not in p.keys():
                return city2
