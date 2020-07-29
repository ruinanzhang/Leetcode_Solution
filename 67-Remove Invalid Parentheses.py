# Tag:Recursion
# 301. Remove Invalid Parentheses
# -----------------------------------------------------------------------------------
# Description:
# Remove the minimum number of invalid parentheses in order to make the input
#  string valid. Return all possible results.
# -----------------------------------------------------------------------------------
# Example 1:

# Input: "()())()"
# Output: ["()()()", "(())()"]

# Example 2:

# Input: "(a)())()"
# Output: ["(a)()()", "(a())()"]

# Example 3:

# Input: ")("
# Output: [""]
# -----------------------------------------------------------------------------------
# Note: The input string may contain letters other than the parentheses ( and ).
# -----------------------------------------------------------------------------------
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# 思路：recursion
# 1. 首先分析什么样的input不是valid的: count'(' != count ')'
# !!!并且在每个位置,from left to right, if count')' > count '(' then -> invalid 
# but if at certain pos: count'(' > count ')', it may still be valid
# 这是parentheses题的特性，需要记住！
# 2. 题目要求remove min parentheses to get a valid string 
# then we can compute the min '('and ')' to be removed from the string in advance 
# 3. Base case: 
# if left_parenthese_to_be_removed == 0  and right_parenthese_to_be_removed == 0
# and isvalid(string):
# !!!这里因为我们要记录所有结果，所以用global stack self.res to record this qualified string:
# self.res.append(string)
# return
# 4. Recursive step:
# For every candidates in string:
# if we know the string removed this candidate will be valid -> remove this candidate 
# else: remove next '(' or ')' untill the string is valid 
# 5. What if duplicates: 
#  if ()) remove the first ) and second ) will end up with the same res: 
#  in this case, if index!=0, only remove the first )
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
      # 1.首先检查s是否valid
      # 2.如果不valid，需要删除几个open_paren 和几个closing_paren
      # 3.scan from left to right, if not valid -> delete
      # - closing_paraen_to_be_deleted -1, record last_deleted index 
      # - continue to next index, until closing_paraen_to_be_deleted== 0 
      # 4.scan from right to left to delet open_paren
        def isValid(string):
            count = 0
            for char in string:
                if char == '(':
                    count +=1
                if char == ')':
                    count -=1
                if count < 0:
                    return False 
            return count == 0
        def par_to_remove(string):
            count = 0
            left_p = 0
            right_p = 0
            for char in string:
                if char == '(':
                    left_p +=1
                if char == ')':
                    if left_p == 0:
                        right_p +=1
                    else:
                        left_p -=1
            return left_p,right_p
        def dfs_delet(s,start_ind,left,right):
            if left == right == 0:
                if isValid(s):
                    self.res.append(s)
                    return 
            while start_ind < len(s):
                if s[start_ind]!=')' and s[start_ind]!='(':
                    start_ind +=1
                    continue
                if s[start_ind] == ')':
                    if right>0:
                        if start_ind == 0 or s[start_ind] != s[start_ind-1]:
                            dfs_delet(s[:start_ind]+s[start_ind+1:],start_ind,left,right-1)
                if s[start_ind] == '(':
                    if left >0:
                        if start_ind == 0 or s[start_ind] != s[start_ind-1]:
                            dfs_delet(s[:start_ind]+s[start_ind+1:],start_ind,left-1,right)
                start_ind +=1
        if isValid(s):
            return [s]
        left, right = par_to_remove(s)
        self.res = []
        dfs_delet(s,0,left,right)
        if not self.res:
            return [""]
        return self.res