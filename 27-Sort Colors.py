# Tag: Sort
# 75. Sort Colors
# -----------------------------------------------------------------------------------
# Description:
# Given an array with n objects colored red, white or blue, sort them in-place so that 
# objects of the same color are adjacent, with the colors in the order red, white and blue.
# Here, we will use the integers 0, 1, and 2 to represent the color red, white, 
# and blue respectively.
# Note: You are not suppose to use the library's sort function for this problem.
# -----------------------------------------------------------------------------------
# Example: 
# Input: [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# 思路：两个ptr！
# 1. 因为有三个颜色，0，1，2  --> Red, White, Blue
# Thus we only need 2 ptrs to indicate colors boundaries: 
# R R R R ... red_right_most W W W ..... Blue_leftmost .... B B B B 
# 2. Use a third ptr Curr to indicate current number: 
#  If nums[curr] == 0: 
#   swap nums[curr] and nums[red_right]
#   red_right ++; curr++
#  Else If nums[curr] == 1:
#   curr++ // do nothing
#  Else If nums[curr] == 2: 
#   swap nums[curr] and nums[blue_left]
#   blue_left -- 
# 3. !!!重点！！！在while loop要用elif，不然会出现同一个条件+1后继续判别的情况！
# 总之平行判别条件用elif总错！！！！❌❌❌
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n == 1:
            return nums
        red_right= 0 
        blue_left = n -1 
        curr = 0 
        while curr <= blue_left:
            if nums[curr] == 0:
                temp = nums[red_right]
                nums[red_right] = nums[curr]
                nums[curr] = temp
                red_right +=1
                curr +=1
            elif nums[curr] == 2:
                temp = nums[blue_left]
                nums[blue_left] = nums[curr]
                nums[curr] = temp
                blue_left -=1
            else:
                curr +=1
        return nums
            