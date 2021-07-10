class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        rook_index, r_row, r_index = self.find_rook(board)

        kills = 0
        for r in board[r_index:]:
            if r[rook_index] == 'B':
                break
            if r[rook_index] == 'p':
                kills += 1
                break
        for r in board[r_index::-1]:
            if r[rook_index] == 'B':
                break
            if r[rook_index] == 'p':
                kills += 1
                break

        for e in r_row[rook_index:]:
            if e == 'B':
                break
            if e == 'p':
                kills += 1
                break
        for e in r_row[rook_index::-1]:
            if e == 'B':
                break
            if e == 'p':
                kills += 1
                break

        return kills

    def find_rook(self, board: List[List[str]]) -> int:
        for index in range(len(board)):
            if "R" in board[index]:
                return (board[index].index('R'), board[index], index)
