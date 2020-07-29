# Tag: Recurssion - Backtracking 
# 37. Sudoku Solver
# -----------------------------------------------------------------------------------
# Description:
# Write a program to solve a Sudoku puzzle by filling the empty cells.

# A sudoku solution must satisfy all of the following rules:

# Each of the digits 1-9 must occur exactly once in each row.
# Each of the digits 1-9 must occur exactly once in each column.
# Each of the the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
# Empty cells are indicated by the character '.'
# -----------------------------------------------------------------------------------
# Note:
# The given board contain only digits 1-9 and the character '.'.
# You may assume that the given Sudoku puzzle will have a single unique solution.
# The given board size is always 9x9.
# -----------------------------------------------------------------------------------
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
#       用backtracking的思路来做！
#       首先就是肯定要分区块，然后每个空位，只有9格内没有的数的
#       因为soduku has two constrians: 
#       A. 同一个九格里面 每一个数字只能出现一次
#       B. 同一row/col： 每一个数字只能出现一次
#       所以在check valid 里面必须要check两个，所以必须给每个数一个box_index  
        def could_fill(digit, i, j):
            # check row
            for y in range(len(board)):
                if self.board[i][y] == str(digit):
                    return False
            # check column
            for x in range(len(board)):
                if self.board[x][j] == str(digit):
                    return False
            # check square
            square_x, square_y = i//3, j//3
            for x in range(square_x*3, square_x*3+3):
                for y in range(square_y*3, square_y*3+3):
                    if self.board[x][y] == str(digit):
                        return False
            return True
            
        def backtracking(row,col):
#           终止条件，如果最后一个格子已经到了，那就说明填完了 
            if col + 1 == N and row+1 == N and self.board[row][col] != '.':
                self.Solved = True
            if self.Solved:
                return True
#           首先检查这个cell是不是空的：
            if self.board[row][col] == '.':
#           再看有没有可以填的数:在这一步要检查两个限制，同时满足才能fill
                for num in range(1,10):
                    if could_fill(num,row,col):
                        self.board[row][col] = str(num)
                        if col + 1 == N and row+1 == N:
                            self.Solved = True
                            return 
#                       如果col到头了，下一个数就要转row了
                        if col == N-1:
                            backtracking(row+1,0)
#                       如果col没有到头，下一个数就是下个col
                        else:
                            backtracking(row,col+1)
#                       如果这条path没有找到结果：
                        if not self.Solved:
                            self.board[row][col] = '.'
                   
            else:
#           看下一个数：
                if col == N-1:
                    backtracking(row+1,0)
                else:
                    backtracking(row,col+1)
        self.Solved = False
        self.board = board
        N = 9
        backtracking(0,0)
        return self.board
            

        