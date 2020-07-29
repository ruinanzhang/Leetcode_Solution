# Tag: Recursion
# 39. Combination Sum
# -----------------------------------------------------------------------------------
# Description:
# Given a set of candidate numbers (candidates) (without duplicates) and a target number (target),
#  find all unique combinations in candidates where the candidate numbers sums to target.
# The same repeated number may be chosen from candidates unlimited number of times.
# -----------------------------------------------------------------------------------
# Example:

# Input: candidates = [2,3,6,7], target = 7,
# A solution set is:
# [
#   [7],
#   [2,2,3]
# ]
# -----------------------------------------------------------------------------------
# Note: 
# All numbers (including target) will be positive integers.
# The solution set must not contain duplicate combinations.
# -----------------------------------------------------------------------------------
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#  思路：recursion：
#  # recursion 👌
          # sub-prob：如果我们能找到target-某个candidate的所有答案，只需要在后面append candidate就ok
          # base case：target == 0
          # Induction step: 找到target-某个candidate的所有答案，只需要在后面append candidate就ok
          # !!!为了避免sol的重复，因为比如【2，2，3】和【3，2，2】其实是一样的，所以在candi是3的时候，不看前面比它小的数能组成的答案，只看它和比他大的数可以组成的所有ans就好了！
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def helper(candidates,target):
            if target == 0:
                return [[]]
            if target < 0:
                return None
            sol = []
            for candi in candidates:
                sub_sol = helper(candidates[candidates.index(candi):],target-candi)
                if sub_sol:
                    for s in sub_sol:
                        s.insert(0,candi)
                        s.sort()
                    sol +=sub_sol
            return sol 
        res = []
        solutions =  helper(candidates,target)
        for sol in solutions:
            if sol not in res:
                res.append(sol)
        return res
        
                
                
            
                    
                    
                
           
                
            
                