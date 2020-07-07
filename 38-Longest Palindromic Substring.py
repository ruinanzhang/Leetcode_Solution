# Tag: String + DP
# 5. Longest Palindromic Substring
# -----------------------------------------------------------------------------------
# Description:
# Given a string s, find the longest palindromic substring in s. 
# You may assume that the maximum length of s is 1000.
# -----------------------------------------------------------------------------------
# Example:
# Input: "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
# -----------------------------------------------------------------------------------
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# 思路：
# 首先两种重复方式：
# a. even case: "abba" -> isPalindromic(s,i,i+1) i is left i +1 is right
# b. odd case: "aba"   ->isPalindromic(s,i,i) 
# isPalindromic(s,l,r):
# while l>=0, r<=n-1 and s[l]= s[r]: l-=1 r+=1
# 然后ab两种重复方式每个ind这么捋一遍
# 记录temp max len 
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
class Solution:
    def longestPalindrome(self, s: str) -> str:
        def isPalin(s,l,r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                    l -= 1
                    r += 1
            return s[l+1:r]
                
        n = len(s)-1
        r = 1
        if not s:
            return ""
        res = s[0]
        maxind = len(res)
         
        for i in range(n):
            temp = s[i]
#             if odd case: "abba":
            curr = isPalin(s,i,i)
#             if even case: "aba"
            if len(curr) > maxind:
                res = curr
                maxind = len(curr)
            curr = isPalin(s,i,i+1)
            if len(curr) > maxind:
                res = curr
                maxind = len(curr)
            i +=1
        return res
                
                
        
        
        
        

