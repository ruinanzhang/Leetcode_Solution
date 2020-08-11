# Tag:Backtracking
# 22. Generate Parentheses
# -----------------------------------------------------------------------------------
# Description:
# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
# -----------------------------------------------------------------------------------
# Example:
# For example, given n = 3, a solution set is:
# [
#   "((()))",
#   "(()())",
#   "(())()",
#   "()(())",
#   "()()()"
# ]
# -----------------------------------------------------------------------------------
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#  思路：Backtracking
#  Operations：each time we can add "(" or ")"
#  Term Con: re_left == re_right == 0 (all added)
#  Limitation: (not valid case => backtrack) : re_left <0 or re_right <0 or re_right<re_left
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        left = right = n
        res = []
        def backtrack(left,right,string):
            #Termination condition:
            if left == 0 and right ==0:
                res.append(string)
            #Limitation:
            if left <0 or right < 0 or right<left:
                return
            backtrack(left-1,right,string+'(')
            backtrack(left,right-1,string+')')
        
        backtrack(left,right,"")
        return res

