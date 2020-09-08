# Tag: DP
# 5. Longest Palindromic Substring
# -----------------------------------------------------------------------------------
# Description: 

# Given a string s, find the longest palindromic substring in s. You may assume that 
# the maximum length of s is 1000.
# -----------------------------------------------------------------------------------
# Examples:

# Example 1:

# Input: "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.

# Example 2:

# Input: "cbbd"
# Output: "bb"
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# 思路：
# Dp 存储 if s[i][j] is palindromic string
# if i == j: dp[i][j] = T
# if j-i <=2 : dp[i][j] depends on if s[i]==s[j]
# if j-1 > 2: 从中心到边上，按中心扩散的填表，只填半边
# for j in range(n):
    # for i in range(j-1,-1,-1):
    # ......
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Use dp[i][j] to store if s[i][j] is palindromic string
        # Init dp:
        n = len(s)
        dp = [[False]*n for _ in range(n)]
        
        res = ""
        max_len = 1
        # For all strings with only one character is a palindrome
        for i in range(n):
            dp[i][i] = True
            res = s[i]
        for j in range(n):
            for i in range(j-1,-1,-1):
                # if len(sub) = 2
                if j-i <3:
                    dp[i][j] = (s[i]==s[j])              
                else:
                    dp[i][j] = dp[i+1][j-1] and s[i]==s[j]
                if dp[i][j] and (j-i+1) >max_len:
                    max_len = j - i+1
                    res = s[i:j+1]
        return res