# Tag: Recursion
# 89. Gray Code
# -----------------------------------------------------------------------------------
# Description:
# The gray code is a binary numeral system where two successive values differ in only one bit.
# Given a non-negative integer n representing the total number of bits in the code, print the
# sequence of gray code. A gray code sequence must begin with 0.
# -----------------------------------------------------------------------------------
# Example 1:
# Input: 2
# Output: [0,1,3,2]
# Explanation:
# 00 - 0
# 01 - 1
# 11 - 3
# 10 - 2
# For a given n, a gray code sequence may not be uniquely defined.
# For example, [0,2,3,1] is also a valid gray code sequence.
# 00 - 0
# 10 - 2
# 11 - 3
# 01 - 1
# -----------------------------------------------------------------------------------
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# 思路1: 
# Recursion!
# Base case: if n == 0 : return [0]
# if n == 1: return [0,1]
# Recursive step: if we know the previous sub_sol, we add 0 or 1 in order of '0110'
# 想过用backtracking但真的太麻烦了判别
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
class Solution:    
    def grayCode(self, n: int) -> List[int]:
        if n == 0:
            return ['0']
        def recursion(n):
            if n == 1:
                return ['0','1']
            solutions = []
            sub_sol =  recursion(n-1)   
            for ind in range(len(sub_sol)):
                if ind % 2 == 0:
                    solutions.append(sub_sol[ind]+'0')
                    solutions.append(sub_sol[ind]+'1')
                else:
                    solutions.append(sub_sol[ind]+'1')
                    solutions.append(sub_sol[ind]+'0')
            return solutions
        res = recursion(n)
        decimal_res = []
        for string in res:
            decimal = int(string,2)
            decimal_res.append(decimal)
        return decimal_res