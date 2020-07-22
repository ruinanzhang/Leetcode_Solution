# Tag: Recurssion - Backtracking 
# 51. N-Queens
# -----------------------------------------------------------------------------------
# Description:
# The n-queens puzzle is the problem of placing n queens on an n×n chessboard 
# such that no two queens attack each other.

# Given an integer n, return all distinct solutions to the n-queens puzzle.

# Each solution contains a distinct board configuration of the n-queens' placement, 
# where 'Q' and '.' both indicate a queen and an empty space respectively.
# -----------------------------------------------------------------------------------
# Input: 4
# Output: [
#  [".Q..",  // Solution 1
#   "...Q",
#   "Q...",
#   "..Q."],

#  ["..Q.",  // Solution 2
#   "Q...",
#   "...Q",
#   ".Q.."]
# ]
# Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above.
# -----------------------------------------------------------------------------------
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
# 用recursion的backtracking来解决类似的问题：
# 一般都是有从第一个candiate开始，往下找next—candidate
# 如果无法找到solution，就清空curr candidate 然后backtrack到上一个可能的candiate
# ！！！特别要注意的是在这一题有两个tips：
# (1) A queen will not exist in same row or col, so eitehr iter col or row is enough 
# (2) For n*n board, there are 2 types of diag : hill or dale 
# For numbers in each diag: for hill-> row-col == const
# for dale ->  row+col == const 
#       **Use this to check if current postion is valid for add a queen
#       Curr pos is valid if this col has no queen as well as hill and dale diag
#       这里的小技巧：同一个diag上的数有一样的 row-col and row+col
        def valid_pos(row,col):
            if (cols[col] + hill_diag[row+col] +dale_diag[row-col]) >= 1:
                return False
            else:
                return True
#       once inser queen，需要把col和对角线门都变成1
        def insert_queen(row,col):
            cols[col] = 1
            hill_diag[row+col] = 1
            dale_diag[row-col] = 1
#       also append the quuen to the queens list:
            queens.append((row,col))
        def remove_queen(row,col):
            cols[col] = 0
            hill_diag[row+col] = 0
            dale_diag[row-col] = 0
            queens.remove((row,col))
        def add_res():
            solution = []
            for _, col in sorted(queens):
                solution.append('.' * col + 'Q' + '.' * (n - col - 1))
            output.append(solution)
            
        def backtrack(row):
            for col in range(n):
                if valid_pos(row,col):
                    insert_queen(row,col)
                    if row + 1 == n:
                        add_res()
                    else:
                        backtrack(row+1)
                    remove_queen(row,col)
        cols = [0]*n
        hill_diag = [0] *(2*n -1)
        dale_diag = [0] *(2*n -1)
        queens =[]
        output = []
        backtrack(0)
        return output
        
             
