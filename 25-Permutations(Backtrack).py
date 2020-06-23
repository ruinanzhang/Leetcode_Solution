# Tag: Recursion+Backtracking
# 46. Permutations
# -----------------------------------------------------------------------------------
# Description:
# Given a collection of distinct integers, return all possible permutations.
# -----------------------------------------------------------------------------------
# Example: 
# Input: [1,2,3]
# Output:
# [
#   [1,2,3],
#   [1,3,2],
#   [2,1,3],
#   [2,3,1],
#   [3,1,2],
#   [3,2,1]
# ]
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# 思路：Recursion+Backtracking
# Swap 第一个char与别的char -> 下一个level -> stop condition: reach the end of the string 

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
class Solution:
    def permute(self, nums):
        def backtrack(index):
            if index == n:
                res.append(nums[:])
            for i in range(index,n):
                # （换index和后面的char的位置）
                nums[index],nums[i] = nums[i],nums[index]
                backtrack(index+1)
                nums[index],nums[i] = nums[i],nums[index]
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        res = []
        backtrack(0)
        return res
        