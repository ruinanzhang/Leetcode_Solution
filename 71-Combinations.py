# Tag:Backtracking
# 77. Combinations
# -----------------------------------------------------------------------------------
# Description:
# Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.
# -----------------------------------------------------------------------------------
# Example:
# Input: n = 4, k = 2
# Output:
# [
#   [2,4],
#   [3,4],
#   [2,3],
#   [1,2],
#   [1,3],
#   [1,4],
# ]
# # -----------------------------------------------------------------------------------
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# 思路1: recursion：
# Base Case:
    # k ==0 : return []
    # Recursive Step: add larger num from number_list to sub_sol every step
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
class Solution1:
    def combine(self, n: int, k: int) -> List[List[int]]:
            num_list = [x for x in range(1,n+1)]
            def recursion(k,num_list):
                if k == 0:
                    return []
                # local var solution 
                solutions = []
                sub_sol = recursion(k-1,num_list)
                if not sub_sol:
                    for i in num_list:
                        solutions.append([i])
                else:
                    for sol in sub_sol:
                        for i in num_list:
                            # 注意这里不是append是concatenate!!!
                            if i>sol[-1] and len(sol)==k-1:
                                solutions.append(sol+[i])
                return solutions
            if k == 0:
                return [[]]
            return recursion(k,num_list)
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# 思路2: backtracking
# Termination condition: len(path) == k
# Limit: len(path) can > k and i should > path[-1] to be added 
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
class Solution2:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        num_list = [x for x in range(1,n+1)]
        def backtracking(path):
            if path: 
                if len(path) == k:
                    res.append(path)
                    return 
                if len(path)>k:
                    return
            for i in range(1,n+1):
                if not path:
                    backtracking([i])
                elif path:
                    if i > path[-1]:
                        backtracking(path+[i])
        backtracking([])
        return res
                