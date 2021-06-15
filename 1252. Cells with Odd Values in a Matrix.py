class Solution(object):
    def oddCells(self, m, n, indices):
        """
        :type m: int
        :type n: int
        :type indices: List[List[int]]
        :rtype: int
        """
        lst = []
        last_indice = len(indices) - 1
        odds = 0
        for i in range(m):
            lst.append([])
            for j in range(n):
                lst[i].append(0)
        for indice in range(len(indices)):
            ind1 = indices[indice][0]
            ind2 = indices[indice][1]
            for _ in range(len(lst[ind1])):
                lst[ind1][_] += 1
            for row in lst:
                row[ind2] += 1
            if indice == last_indice:
                for row in lst:
                    for num in row:
                        if num % 2 != 0:
                            odds += 1
        return odds
