'''
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:
A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
'''

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for i in range(9):
            d={}
            for j in range(9):
                if board[i][j].isdigit():
                    if board[i][j] in d:
                        return False
                    d[board[i][j]]=1
        
        for i in range(9):
            d={}
            for j in range(9):
                if board[j][i].isdigit():
                    if board[j][i] in d:
                        return False
                    d[board[j][i]]=1
            
        for k in range(1,4):
            d1={}
            d2={}
            d3={}
            for i in range(3*(k-1),3*k):
                for j in range(9):
                    if j<3:
                        if board[i][j].isdigit():
                            if board[i][j] in d1:
                                return False
                            d1[board[i][j]]=1
                    elif j<6:
                        if board[i][j].isdigit():
                            if board[i][j] in d2:
                                return False
                            d2[board[i][j]]=1
                    else:
                        if board[i][j].isdigit():
                            if board[i][j] in d3:
                                return False
                            d3[board[i][j]]=1
        return True
