# Tag: Matrix
# 973. K Closest Points to Origin
# -----------------------------------------------------------------------------------
# Description:
# # (0,0)
# ---------------------------
# |                         |
# |           (r1,c1)       |
# |             |-----------|(r1,c2)
# |             |  RegionA  |
# | ------------------------|(r2,c2)
# |           (r2,c1)       |
#  --------------------------
#  RegionA = region(0,0 to r2,c2) - 
#       region(0,0 to r2,c1) - 
#       region(0,0 to r1,c2) + 
#       region(0,0 to r1,c1)
#  
# Given a 2D matrix matrix, find the sum of the elements inside the rectangle defined 
# by its upper left corner (row1, col1) and lower right corner (row2, col2).
# Range Sum Query 2D
# The above rectangle (with the red border) is defined by (row1, col1) = (2, 1) and 
# (row2, col2) = (4, 3), which contains sum = 8.
# -----------------------------------------------------------------------------------
# Example:
# Given matrix = [
#   [3, 0, 1, 4, 2],
#   [5, 6, 3, 2, 1],
#   [1, 2, 0, 1, 5],
#   [4, 1, 0, 1, 7],
#   [1, 0, 3, 0, 5]
# ]

# sumRegion(2, 1, 4, 3) -> 8
# sumRegion(1, 1, 2, 2) -> 11
# sumRegion(1, 2, 2, 4) -> 12
# -----------------------------------------------------------------------------------
# Note:
# You may assume that the matrix does not change.
# There are many calls to sumRegion function.
# You may assume that row1 ≤ row2 and col1 ≤ col2
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# 思路：
# 因为有很多重复所以2d array table先全算一遍
# 注意右下角边界是全+1算，这样不怕最开始出界，只要inti成0就ok了
# 在 row1 col1 其实是 要 +1-1 ->才是sum对应的边界，sum都是本身的数+1算的底角因为
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        if not matrix:
            return
        self.matrix = matrix
        n = len(self.matrix)
        m = len(self.matrix[0])
        self.sum = [[0 for j in range(m+1)] for i in range(n+1)]
        for i in range(1,n+1):
            for j in range(1,m+1):
                self.sum[i][j] = matrix[i-1][j-1] + self.sum[i][j-1] + self.sum[i-1][j] - self.sum[i-1][j-1]
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        top = self.sum[row1+1-1][col1+1-1]
        left = self.sum[row2+1][col1+1-1]
        over = self.sum[row1+1-1][col2+1]
        return self.sum[row2+1][col2+1] - left - over + top         
         