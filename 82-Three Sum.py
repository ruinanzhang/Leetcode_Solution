# Tag: Two Pointers
# 15. 3Sum
# -----------------------------------------------------------------------------------
# Description:

# Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? 
# Find all unique triplets in the array which gives the sum of zero.
# -----------------------------------------------------------------------------------
# Note:

# The solution set must not contain duplicate triplets.
# -----------------------------------------------------------------------------------
# Example:

# Given array nums = [-1, 0, 1, 2, -1, -4],
# A solution set is:
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]
# -----------------------------------------------------------------------------------
# 两指针做法 + .sort()
# Two Pointers 
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        left = 0
        right = len(nums)-1
        res = []
        for i in range(len(nums)):
            if nums[i]>0:
                break
            if i == 0 or nums[i]!= nums[i-1]:
                left = i+1
                right = len(nums)-1
                while left < right:
                    total = nums[left] + nums[right] + nums[i]
                    if total ==0:
                        res.append([nums[i],nums[left],nums[right]])
                        left +=1
                        right -=1
                        while left < right  and nums[left] == nums[left-1]:
                            left+=1
                    elif total < 0:
                        left +=1
                    elif total > 0:
                        right-=1
        return res