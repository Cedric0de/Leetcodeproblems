class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        hashcol = {}
        hashrow = {}
        box = {}
        
        for i in range(9):
            for x in range(9):
                if board[i][x] == ".":
                    continue
                if((board[i][x] in hashrow[i]) or (board[i][x] in hashcol[x]) or (board[i][x] in box[i // 3, x // 3])):
                    return False
                hashcol[x].add(board[i][x])
                hashrow[i].add(board[i][x])
                box[i // 3, c // 3].add(board[i][x])
        return True