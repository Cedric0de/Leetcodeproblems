class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        rows = [set() for i in range(9)]
        columns = [set() for i in range(9)]
        squares = [[set() for i in range(3)] for x in range(3)]
        
        for i in range(9):
            for x in range(9):
                cell_value = board[i][x]
                if cell_value == ".":
                    continue
                if cell_value in rows[i] or cell_value in columns[x] or cell_value in squares[i//3][x//3]:
                    return False

                rows[i].add(cell_value)
                columns[x].add(cell_value)
                squares[i//3][x//3].add(cell_value)
        
        return True