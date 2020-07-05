# Tag: DP / Heap
# 264. Ugly Number II
# -----------------------------------------------------------------------------------
# Description:
# Write a program to find the n-th ugly number.
# Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. 
# -----------------------------------------------------------------------------------
# Example:
# Input: n = 10
# Output: 12
# Explanation: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.
# -----------------------------------------------------------------------------------
# Note: 
# 1 is typically treated as an ugly number.
# n does not exceed 1690.
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# 思路：
# 👌👌👌 Dynamic Programming 
# The algorithm is straightforward: 
# choose the smallest ugly number among nums[p2]*2,nums[p3]*3,nums[p5]*5)
# and add it into the array. Move the corresponding pointer by one step. 
# Repeat till you'll have 1690 ugly numbers.
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        nums = [1,]
        
        def getNums(p2,p3,p5):
            for i in range(1690):
                
                nextUgly = min(nums[p2]*2,nums[p3]*3,nums[p5]*5)
                nums.append(nextUgly)
                if nums[p2]*2 == nextUgly:
                    p2+=1
                if nums[p3]*3 == nextUgly:
                    p3+=1
                if nums[p5]*5 == nextUgly:
                    p5+=1
                    
        getNums(0,0,0)
        return nums[n-1]