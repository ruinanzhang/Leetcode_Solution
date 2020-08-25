# Tag: Matrix 
# 48. Rotate Image
# -----------------------------------------------------------------------------------
# Description: 

# You are given an n x n 2D matrix representing an image.
# Rotate the image by 90 degrees (clockwise).
# -----------------------------------------------------------------------------------
# Note:

# You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation
# -----------------------------------------------------------------------------------
# Example 1:
# Given input matrix = 
# [
#   [1,2,3],
#   [4,5,6],
#   [7,8,9]
# ],
# rotate the input matrix in-place such that it becomes:
# [
#   [7,4,1],
#   [8,5,2],
#   [9,6,3]
# ]
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# 思路：
# 1. 一个骚🐶做法：先tanspose再reverse一行
# 2. 正常的做法，但需要数学推到位置：
# (a) 观察可看出，在正方形顶点的数都是四个依次换顺序
# (b) 有几个在这样的正方形呢？-> row_layer == n+1 //2 for col 
#  col_layer == n//2 
# (c) 顶点互换：row,col = col,n-1-row
# 
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n= len(matrix)
        for layer in range((n+1)//2):
            for index in range(n//2):
                temp = [0]*4
                row,col = layer, index
                for k in range(4):
                    temp[k] = matrix[row][col]
                    row,col = col,n-1-row
                for k in range(4):
                    matrix[row][col] = temp[(k - 1) % 4]
                    row, col = col, n - 1 - row