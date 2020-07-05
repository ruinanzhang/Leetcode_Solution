# Tag: Array 特殊算法
# 31. Next Permutation
# -----------------------------------------------------------------------------------
# Description:
# Implement next permutation, which rearranges numbers into 
# the lexicographically next greater permutation of numbers.
# If such arrangement is not possible, it must rearrange it as the
# lowest possible order (ie, sorted in ascending order).
# The replacement must be in-place and use only constant extra memory.
# -----------------------------------------------------------------------------------
# Example: 
# Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
# 1,2,3 → 1,3,2
# 3,2,1 → 1,2,3
# 1,1,5 → 1,5,1
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# 思路：一个神奇的特殊算法：
# 1. 从右到左，先找到第一个不是increase的number index  is i 
# 2. 从i开始往右，找到第一个不是decrese的number，index is j
# 3. swap nums[i] and nums[j]
# 4. Reverse nums[i+1] to nums' end 
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
class Solution:
       def nextPermutation(self, nums):
        i = j = len(nums)-1
        while i > 0 and nums[i-1] >= nums[i]:
            i -= 1
        if i == 0:   # nums are in descending order
            nums.reverse()
            return 
        k = i - 1    # find the last "ascending" position
        while nums[j] <= nums[k]:
            j -= 1
        nums[k], nums[j] = nums[j], nums[k]  
        l, r = k+1, len(nums)-1  # reverse the second part
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l +=1 ; r -= 1