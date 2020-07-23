# Tag: Recurssion - Backtracking 
# 79. Word Search
# -----------------------------------------------------------------------------------
# Description:
# Given a 2D board and a word, find if the word exists in the grid.
# The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells 
# are those horizontally or vertically neighboring. The same letter cell may not be used more than once.
# -----------------------------------------------------------------------------------
# Example:
# board =
# [
#   ['A','B','C','E'],
#   ['S','F','C','S'],
#   ['A','D','E','E']
# ]

# Given word = "ABCCED", return true.
# Given word = "SEE", return true.
# Given word = "ABCB", return false.
# -----------------------------------------------------------------------------------
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# 思路：backtracking
#   backtracking的template：
#   1. def backtracking:
#         if found_solition:
#               early return
#         else:(if haven't found solution)
#         for candidates in next_candidates_list:
#             (a)check if pos is valid ->if not return False
#             (b)check if qualified -> if not return False 
#             (c)mark candidate as vsisted 
#             (d)if (a)(b) qualified -> backtrakcking(next_candidate)
#             (d)如果中途return了要往回走把 visited 清空 -> remove status
#  2. for all posible start point:
#         if found_solution:
#             return (终止运行)
          # backtracking(start_point)
#     如果所有都iter了一遍也没找到：
#     return 没找到/结果
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        def valid_pos(row,col):
            if row<0 or col<0:
                return False
            if row>=len_row or col >=len_col:
                return False
            if visit_map[row][col] ==1:
                return False
            return True
        def match_words(row,col,char):
            if board[row][col] == char:
                return True
            return False
        def next_can(row,col):
            nei = []
            for x_offset,y_offset in [(0, 1), (-1, 0), (0, -1), (1, 0)]:
                nei.append((row+x_offset,col+y_offset))
            return nei
        def backtracking(row,col,curr_word):
#           因为word需要match一个，截掉前面的一个，所以如果pass in的curr_word已经没有了，就说明在backtracking之前的时候已经找到了
            if len(curr_word)==0:
                self.Found = True
            if self.Found:
                return True
#           用backtracking的思路，先check if current pos is valid:
            if not valid_pos(row,col):
                return False
            if not match_words(row,col,curr_word[0]):
                return False
            visit_map[row][col]=1
            next_candidates = next_can(row,col)
            for next_row,next_col in next_candidates:
                if self.Found:
                    break
                backtracking(next_row,next_col,curr_word[1:])
            visit_map[row][col]=0
            
        
        len_row = len(board)
        len_col = len(board[0])
        visit_map = [[ 0 for i in range(len_col) ] for j in range(len_row)] 
        self.Found = False
        for row in range(len_row):
            for col in range(len_col):
#               如果在这个位置开始的某个str已经找到了solution
                if self.Found:
                    return True
                backtracking(row,col,word)
#       如果都没找到：
        return self.Found