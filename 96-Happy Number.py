# Tag:  Simple recursion
# 202. Happy Number
# -----------------------------------------------------------------------------------
# Description: 

# Write an algorithm to determine if a number n is "happy".

# A happy number is a number defined by the following process: Starting with any positive 
# integer, replace the number by the sum of the squares of its digits, and repeat the 
# process until the number equals 1 (where it will stay), or it loops endlessly in a 
# cycle which does not include 1. Those numbers for which this process ends in 1 are 
# happy numbers.

# Return True if n is a happy number, and False if not.
# -----------------------------------------------------------------------------------
# Example:

# Input: 19
# Output: true
# Explanation: 
# 12 + 92 = 82
# 82 + 22 = 68
# 62 + 82 = 100
# 12 + 02 + 02 = 1
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# 思路：
# Simple recursion:
# 两个function： 一个cal：每位的sum
# 一个recursivly 算下一位sum并且对比
# 注意stack for seen 来 checkloop
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
class Solution:
    def isHappy(self, n: int) -> bool:
        seen = []
        def sqr_sum(number):
            sum = 0
            while number:
                re =number%10
                number = number//10
                sum+= re*re
            return sum
        def recursion(prev):
            if prev in seen:
                return False
            else:
                seen.append(prev)
            if prev == 1:
                return True
            curr = sqr_sum(prev)
            if prev == curr:
                return False
            return recursion(curr)
        return recursion(n)
       