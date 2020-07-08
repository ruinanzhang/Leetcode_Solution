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
# 😄第一种做法：not dp：
# 首先两种重复方式：
# a. even case: "abba" -> isPalindromic(s,i,i+1) i is left i +1 is right
# b. odd case: "aba"   ->isPalindromic(s,i,i)
# isPalindromic(s,l,r):
# while l>=0, r<=n-1 and s[l]= s[r]: l-=1 r+=1
# 然后ab两种重复方式每个ind这么捋一遍
# 记录temp max len

class Solution:
    def longestPalindrome(self, s: str) -> str:
        def isPalin(s, l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l+1:r]

        n = len(s)-1
        if not s:
            return ""
        res = s[0]
        maxind = len(res)
        for i in range(n):
            # if odd case: "abba":
            curr = isPalin(s, i, i)
#             if even case: "aba"
            if len(curr) > maxind:
                res = curr
                maxind = len(curr)
            curr = isPalin(s, i, i+1)
            if len(curr) > maxind:
                res = curr
                maxind = len(curr)
            i += 1
        return res

# 👌👌👌👌👌👌👌👌👌👌👌👌👌👌👌👌👌👌重点！dp 做法！！！
# 搞一个table dp！！！！
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
class Solution:
    def longestPalindrome(self, s: str) -> str:
#     用dp，首先init一个table len(n) * len(n):
        n = len(s)
        dp_table = [[False] * n for x in range(n)]
#     In this table, use T or F to represent if substr[i,j] (which means substring range from i to j) is palindrome or not
#     It's obvious to see that all numbers on the diagonal is palindrome cuz they only has one number
        max_len = 0
        res = ""
        for i in range(n):
            dp_table[i][i] = True 
            max_len = 1
            res = s[i]
#     We can also infer that for s[i][j] if j = i+1, then if s[i]= s[i+1] -> palindrom, otherwise return Flase
        for i in range(n-1):
            if s[i] == s[i+1]:
                dp_table[i][i+1] = True
                max_len = 2
                res = s[i:i+2]
            else: 
                dp_table[i][i+1] = False
        # for i in range(n):
        #     for j in range(n):
        #         if j<i:
        #             dp_table[i][j] = False
        for j in range(n):
            for i in range(j-1):
                if s[i] == s[j] and dp_table[i+1][j-1]:
                    dp_table[i][j] = True
                    if max_len < len(s[i:j+1]):
                        max_len = len(s[i:j+1])
                        res = s[i:j+1]

        
        return res