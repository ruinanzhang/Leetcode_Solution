# Tag: DP
# 91. Decode Ways
# -----------------------------------------------------------------------------------
# Description: 

# A message containing letters from A-Z is being encoded to numbers using the 
# following mapping:
# 'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26
# Given a non-empty string containing only digits, determine the total number of ways to decode it.
# -----------------------------------------------------------------------------------
# Example 1:
# Input: "12"
# Output: 2
# Explanation: It could be decoded as "AB" (1 2) or "L" (12).

# Example 2:
# Input: "226"
# Output: 3
# Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# 思路：
# 这题如果用backtrakcing也能做但是会超时
# 所以用dynamic programming做：
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
class Solution:
    def numDecodings(self, s: str) -> int:
        # 定义 DP array to store no of decode ways till index i
        dp = [0 for _ in range(len(s))]
        # if the very first char is 0, there's no way to decode 
        if s[0] == "0":
            return 0
        # if the first char is not "0", it must have one way to decode it as single number
        dp[0] = 1
        for i in range(1,len(s)):
            if s[i]!="0":
                dp[i] = dp[i-1]
            num = int(s[i-1:i+1])  
            if num>=10 and num<=26:
                if i == 1:
                    dp[i] +=1
                else:
                    dp[i]+=dp[i-2]
        return dp[len(s)-1]