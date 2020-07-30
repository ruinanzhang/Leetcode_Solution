# Tag:Recursion
# 78. Subsets
# -----------------------------------------------------------------------------------
# Description:
# Given a set of distinct integers, nums, return all possible subsets (the power set).
# -----------------------------------------------------------------------------------
# Example:
# Input: nums = [1,2,3]
# Output:
# [
#   [3],
#   [1],
#   [2],
#   [1,2,3],
#   [1,3],
#   [2,3],
#   [1,2],
#   []
# ]
# -----------------------------------------------------------------------------------
# Note: The solution set must not contain duplicate subsets.
# -----------------------------------------------------------------------------------
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
#       Base case: 
#       if only one number: 2 possible ans: either number in or not in
#           return [[],[number]]
#       Recursive Step: 
#       if we know all possible ans of the sub_string 
#       curr = curr_number
#       for each a in ans:
#           sol.append([]+a)
#           sol.append([curr]+a)
        def recursion(nums):
            if len(nums) == 1:
                return [[],[nums[0]]]
            sol = []
            sub_ans = recursion(nums[:len(nums)-1])
            curr_num = nums[len(nums)-1]
            for a in sub_ans:
                sol.append([curr_num] + a)
                sol.append([]+a)
            return sol
        return recursion(nums)
            
# Time and space : O(N*2^N) why???
