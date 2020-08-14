# Tag: Recursion / Backtracking
# 90. Subsets II
# -----------------------------------------------------------------------------------
# Description:
# Given a collection of integers that might contain duplicates, nums, return all 
# possible subsets (the power set).
# Note: The solution set must not contain duplicate subsets.
# -----------------------------------------------------------------------------------
# Input: [1,2,2]
# Output:
# [
#   [2],
#   [1],
#   [1,2,2],
#   [2,2],
#   [1,2],
#   []
# ]
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# 思路：Backtracking
# DFS 的同时用“i>index and nums[i]==nums[i-1]” 来rule out 重复的cases！
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
from collections import deque
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        def dfs_backtracking(nums,index,path):
            res.append(path)
            for i in range(index,len(nums)):
                if i>index and nums[i]==nums[i-1]:
                    continue
                else:
                    dfs_backtracking(nums,i+1,path+[nums[i]])
        dfs_backtracking(nums,0,[])     
        return res
            
       









res = []
        N = len(nums)
        nums.sort()
        hash_map = [False]*len(nums)
        def recursion(n):
            #Base Case:
            if n == 0:
                res.append([])
                return [[]]
            #Recursive Step:
            solutions = []
            sub_sol = recursion(n-1)
            hash_map = [False]*len(nums)
            for sol in sub_sol:
                for index in range(len(nums)):
                    if index > 1 and nums[index] == nums[index-1]:
                        continue
                    else:
                        if not sol:
                            solutions.append(sol+[nums[index]])
                            hash_map[index] = True
                        elif nums[index] >= sol[-1] and not hash_map[index]:
                            solutions.append(sol+[nums[index]])
                            hash_map[index] = True
            res.append(solutions)
            return solutions
        recursion(N)
        return res