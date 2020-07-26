# Tag: Recursion
# 40. Combination Sum II
# -----------------------------------------------------------------------------------
# Description:
# Given a collection of candidate numbers (candidates) and a target number (target), 
# find all unique combinations in candidates where the candidate numbers sums to target.
# Each number in candidates may only be used once in the combination.
# -----------------------------------------------------------------------------------
# Example:

# Input: candidates = [10,1,2,7,6,1,5], target = 8,
# A solution set is:
# [
#   [1, 7],
#   [1, 2, 5],
#   [2, 6],
#   [1, 1, 6]
# ]
# -----------------------------------------------------------------------------------
# Note: 
# All numbers (including target) will be positive integers.
# The solution set must not contain duplicate combinations.
# -----------------------------------------------------------------------------------
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# class Solution:
#     def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
#         def helper(candidates,target):
#             if target < 0:
#                 return []
#             if target ==0 :
#                 return [[]]
            
#             sol = []
#             for ind in range(len(candidates)):
#                 if ind > 1 and candidates[ind] == candidates[ind-1]:
#                     continue
#                 sub_can = candidates[ind+1:]
#                 sub_sol = helper(sub_can,target-candidates[ind])
#                 if sub_sol:
#                     for s in sub_sol:
#                         s.append(candidates[ind])
#                     sol+=sub_sol
#             return sol
#         candidates.sort()   
#         return helper(candidates,target)
class Solution:
    def combinationSum2(self, candidates, target):
        answer = []
        candidates = sorted(candidates)
        self.dfs(candidates, target, 0, [], answer)
        return answer

    def dfs(self, candidates, target, index, path, answer):
        if target < 0:
            return  # backtracking
        if target == 0:
            answer.append(path)
            return  # backtracking 
        for i in range(index, len(candidates)):
            if i == index or candidates[i] != candidates[i-1]:
                # if we are on the first index
                # OR
                # if we are not the same as the previous number so think 1,1,2,5 (target = 8) (you don't want to go through the tree starting with 1 (on the second branch))
                self.dfs(candidates, target-candidates[i], i + 1, path + [candidates[i]], answer)
                
            
        