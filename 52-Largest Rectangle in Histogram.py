# Tag: Monotonic Stack!!!!
# 84. Largest Rectangle in Histogram
# -----------------------------------------------------------------------------------
# Description:
# Given n non-negative integers representing the histogram's bar height where the width of each bar 
# is 1, find the area of largest rectangle in the histogram.
# -----------------------------------------------------------------------------------
# Example 1:
# Input: [2,1,5,6,2,3]
# Output: 10
# -----------------------------------------------------------------------------------

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# 思路：
#   用递增单调栈来解题
#   递增单调栈->每个数之前的那个数就是previous greater number
#   每个数入stack的时候就是被iter的时候
#   每个数出stack的时候是重点！！！
#   When the number is poped out of our monotonic + stack:
#   We found the next number smaller than this number 
#   因为要找的是最大面积的长方形，所以the top of rect muxt be the smallest bar
#   那么当pop掉某个数的时候，我们已经知道
#   between the new added num and the num to be popded, 
#   all the numbers in between are larger than the the num to be popded
#   !!!And 因为在the num to be popded之前有可能也有可能有比它大的数但是已经被pop掉了
#   所以我们要找的区间就是【pre—比pop数小的数，next—比pop数小的数】
#   那么很显然，在pop数前比pop数小的数就是pop数在monotonic stack中的前一位数
#   next—比pop数小的数就是当前要pop这个数的数
#   那么被pop数最大可以的宽度len就是 curr index - previous_index_of_pop_num's -1 
#   （-1）是因为不能算curr index的宽度～
#   这里需要注意！！！如果pop数之前没有数了，就说明pop数之前所有都比pop数小，所以pre index设为-1
#   so for the num to be poped, largest area(S) =len*h
#   我们还需要一个global var 来store到当前位置最大面积，如果之后有比他大的再更新！
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        monotonic_stack = []
        n = len(heights)
        heights.append(-1)
#       注意这里要加个-1保证最后一个bar也会被算到！！！！
        max_rect = 0
        for ind in range(n+1):
            while monotonic_stack and heights[ind]<=heights[monotonic_stack[-1]]:
                curr_pop_height = heights[monotonic_stack[-1]]
                monotonic_stack.pop()
                if not monotonic_stack:
                     width = ind
                else:
                    width = ind - monotonic_stack[-1] - 1
                local_rect = curr_pop_height*width
                if local_rect > max_rect:
                    max_rect = local_rect 
            monotonic_stack.append(ind)
        return max_rect