# Tag: Math + Stirng
# 67. Add Binary
# -----------------------------------------------------------------------------------
# Description:
# Given two binary strings, return their sum (also a binary string).
# The input strings are both non-empty and contains only characters 1 or 0.
# -----------------------------------------------------------------------------------
# Example 1:
# Input: a = "11", b = "1"
# Output: "100"
# -----------------------------------------------------------------------------------

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# 思路：
#   1. bit+bit comparision: 用一个plus来表示进位数
#   2. convert a&b to int, do sum -> map back to binary 
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# 解法1: 
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        len_a = len(a)
        len_b = len(b)
        if len_a >= len_b:
            l = a
            s = b
        else: 
            l = b
            s = a
        for i in range(len(l) - len(s)):
            s="0"+s
        plus = 0
        res = ""
        for i in range((len(l)-1),-1,-1):
            if int(l[i])+int(s[i])+plus == 0:
                res ="0" + res
                plus = 0
            elif int(l[i])+int(s[i])+plus == 1:
                res ="1" + res
                plus =0
            elif int(l[i])+int(s[i])+plus == 2:
                res ="0" + res
                plus =1
            elif int(l[i])+int(s[i])+plus == 3:
                res ="1" + res
                plus =1
        if plus ==1:
            res = "1" + res
        return res
#解法2：
class Solution:
    def addBinary(self, a, b) -> str:
        # !!!!!重点{0:b}' 就是map int to binary and include in a string 
        return '{0:b}'.format(int(a, 2) + int(b, 2))
     