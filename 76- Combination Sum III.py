# Tag: Backtracking
# 216. Combination Sum III
# -----------------------------------------------------------------------------------
# Description:
# Find all possible combinations of k numbers that add up to a number n, given that 
# only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.
# -----------------------------------------------------------------------------------
# Note:
# All numbers will be positive integers.
# The solution set must not contain duplicate combinations.
# -----------------------------------------------------------------------------------
#Example 1:
# Input: k = 3, n = 7
# Output: [[1,2,4]]

# Example 2:
# Input: k = 3, n = 9
# Output: [[1,2,6], [1,3,5], [2,3,4]]
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# 思路：
# BackTracking 
# Term Condition: len(path) == k, total = 0
# Limitation: no dup, so everytime on recursive step, 
# only check candidates that's larger than current number 
# Operation: sum - num
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        def backtracking(total,path,index):
            if len(path) == k:
                if total == 0:
                    res.append(path[:])
                return
            for i in range(index,10): 
                path.append(i)
                backtracking(total-i,path,i+1)
                path.pop()
        backtracking(n,[],1)
        return res