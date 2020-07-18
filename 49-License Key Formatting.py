# Tag: String
# License Key Formatting
# -----------------------------------------------------------------------------------
# Description:
# You are given a license key represented as a string S which consists only alphanumeric 
# character and dashes. The string is separated into N+1 groups by N dashes.

# Given a number K, we would want to reformat the strings such that each group contains 
#  exactly K characters, except for the first group which could be shorter than K,
#  but still must contain at least one character. Furthermore, there must be a dash inserted
#  between two groups and all lowercase letters should be converted to uppercase.

# Given a non-empty string S and a number K, format the string according to the rules described above.
# -----------------------------------------------------------------------------------
# Example 1:
# Input: S = "5F3Z-2e-9-w", K = 4

# Output: "5F3Z-2E9W"

# Explanation: The string S has been split into two parts, each part has 4 characters.
# Note that the two extra dashes are not needed and can be removed.
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# 思路：
# 首先熟悉一下python string的操作：
# S = "ABCDE" char = 6
# 1. insert char to S aftet C: S[:3] + char + [3:]
# 2. remove A from S: S.replace("A","")
# 之后就是看余数决定开头，loop一下，用start end来slice string
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        
        S = S.upper().replace("-","")
        n = len(S)
        re = n%K
        da = "-"
        res = ""
        if n <=K:
            return S
        if re != 0:
            start = re
            res = S[:start] + da
        else:
            start = 0
        end = re + K

        while end < n:
                res +=S[start:end]+da     
                start = end
                end += K
        res = res + S[start:]
        
        return res
            
        