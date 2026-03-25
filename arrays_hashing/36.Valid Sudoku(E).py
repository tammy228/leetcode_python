"""
My Solution

use three list of set to record row, col, square rules while iterating wholde board

Time:
O(N^2), for 3x3 sudoku it will always be O(81)

Space:
O(N^2), for 3x3 sudoku it will always be O(81 * 3)
"""
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for i in range(9)]
        cols = [set() for i in range(9)]
        squares = [set() for i in range(9)]
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] != '.':
                    # idx = int(i / 3) * 3 + int(j / 3)
                    # change to more pythonic style
                    idx = (i // 3) * 3 + (j // 3)
                    if board[i][j] in rows[i] or board[i][j] in cols[j] or board[i][j] in squares[idx]:
                        return False
                    cols[j].add(board[i][j])
                    rows[i].add(board[i][j])
                    squares[idx].add(board[i][j])
        return True
