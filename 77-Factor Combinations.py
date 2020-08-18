# Tag: Backtracking
# 254. Factor Combinations
# -----------------------------------------------------------------------------------
# Description:
# Numbers can be regarded as product of its factors.
# For example,
# 8 = 2 x 2 x 2;
#   = 2 x 4.
# Write a function that takes an integer n and return all possible combinations of its factors.
# -----------------------------------------------------------------------------------
# Note:
# You may assume that n is always positive.
# Factors should be greater than 1 and less than n.
# -----------------------------------------------------------------------------------
# Example 1:
# Input: 1
# Output: []

# Example 2:
# Input: 37
# Output:[]

# Example 3:
# Input: 12
# Output:
# [
#   [2, 6],
#   [2, 2, 3],
#   [3, 4]
# ]
# -----------------------------------------------------------------------------------
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# 思路：
# BackTracking 
# Term Condition: sub_totoal == 1 
# Limitation: 1. sub_totoal % number == 0 
# 2. Avoid path dup: only check candidates that's equal or larger than current number 
# Operation: sum//n (for i in range(index, sub_total))
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        if n == 1:
            return []
        res = []
        def backtrakcing(sn,path,index):
            if sn == 1:
                res.append(path[:])
                return
            for i in range(index,sn+1):
                if sn%i == 0:
                    if i!= n:
                        path.append(i)
                        backtrakcing(sn//i,path,i)
                        path.pop()
        backtrakcing(n,[],2)
        return res
        