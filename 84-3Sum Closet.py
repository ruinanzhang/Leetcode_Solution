# Tag: Two Pointers + Recursion
# 16. 3Sum Closest
# -----------------------------------------------------------------------------------
# Description: 

# Given an array nums of n integers and an integer target, find three integers in nums 
# such that the sum is closest to target. Return the sum of the three integers. You may 
# assume that each input would have exactly one solution.
# -----------------------------------------------------------------------------------
# Note:

# 3 <= nums.length <= 10^3
# -10^3 <= nums[i] <= 10^3
# -10^4 <= target <= 10^4
# -----------------------------------------------------------------------------------
# Example 1:

# Input: nums = [-1,2,1,-4], target = 1
# Output: 2
# Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
# -----------------------------------------------------------------------------------
# 还是用两支针，recursivly call 2sum-closet function

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        if len(nums) == 3:        
            return sum(nums)
        def find_2sum_closest(target,nums):
            left = 0
            right = len(nums)-1
            min_w_tar = target - (nums[left] + nums[right])
            while left < right:
                twosum = nums[left] + nums[right]
                local_min = target - twosum
                if abs(local_min) < abs(min_w_tar):
                        min_w_tar = local_min
                if twosum <= target or (left > 0 and nums[left] == nums[left-1]):
                    left += 1
                elif twosum > target or (right <len(nums)-1 and nums[right] == nums[right+1]):
                    right -= 1
            return target - min_w_tar
        closet = nums[0]+nums[1]+nums[2]
        for i in range(len(nums)-2):
            if i == 0 or nums[i]!=nums[i-1]:
                sub_sum = find_2sum_closest(target-nums[i],nums[i+1:])
                sub_min = target - (sub_sum +nums[i])
                if abs(sub_min) <= abs(target-closet):
                    closet = sub_sum +nums[i]
        return closet