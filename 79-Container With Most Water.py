# Tag: Array/2 ptrs
# 11. Container With Most Water
# -----------------------------------------------------------------------------------
# Given n non-negative integers a1, a2, ..., an , where each represents a point at 
# coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line 
# i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a 
# container, such that the container contains the most water.

# Note: You may not slant the container and n is at least 2
# -----------------------------------------------------------------------------------
# Example:
# Input: [1,8,6,2,5,4,8,3,7]
# Output: 49
# -----------------------------------------------------------------------------------
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# 思路：
# 感觉也可以用mono stack做但需要两个stack因为有height 还有width
# 用2 ptr，更新短的板子，因为2板之间的s取决于短的那个
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) -1
        max_s = 0
        while left < right:
            if height[left]<=height[right]:
                s = (right-left)*(height[left])
                if s > max_s:
                    max_s = s
                left +=1
            else:
                s = (right-left)*(height[right])
                if s > max_s:
                    max_s = s
                right -=1
        return max_s
                                         
                