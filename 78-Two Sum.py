# Tag: HashTable
# 1. Two Sum
# -----------------------------------------------------------------------------------
# Description:
# Given an array of integers, return indices of the two numbers such that they
#  add up to a specific target.
# You may assume that each input would have exactly one solution, and you may 
# not use the same element twice.
# -----------------------------------------------------------------------------------
# Example:
# Given nums = [2, 7, 11, 15], target = 9,
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].
# -----------------------------------------------------------------------------------
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#Since we are only looking for 2 sum, so no backtrack!!!
#Use hash table
# 时间是O(n)因为iter一遍，num的位置，target-num如果在，直接返回index
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i, num in enumerate(nums):
            if target-num in d:
                return d[target-num], i
            d[num] = i
        
           