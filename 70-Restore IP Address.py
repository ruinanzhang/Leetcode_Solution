# Tag:Backtracking
# 93. Restore IP Addresses
# -----------------------------------------------------------------------------------
# Description:
# Given a string containing only digits, restore it by returning all possible valid 
# IP address combinations.
# A valid IP address consists of exactly four integers (each integer is between 0 and 255)
# separated by single points.
# -----------------------------------------------------------------------------------
# Example:
# Input: "25525511135"
# Output: ["255.255.11.135", "255.255.111.35"]
# -----------------------------------------------------------------------------------
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
class Solution:
    def restoreIpAddresses(self, s):
      # 思路：backtracking 
      # Term Condition: in total 4 ints are generated and no more left digits
      # Limitation: 1. not latger than 255 , not smaller than 0 or start with 0
      # 操作：选择1or2or3digits后加‘.’!!!主要画图的时候还是注意每一步（每一个分支）可以做什么operation
        res = []
        length = len(s)
        def backtracking_dfs(split_times,start,s,sub_path):
            # Term Condition
            if start == length and split_times == 4:
                res.append(sub_path[:-1])
                return
            if split_times >=4 and start <= length:
                return 
            for i in range(1,4):
                if i!= 1 and s[start] == '0':
                    return
                if length-start < i or length-start>3*(4-split_times):
                    return
                if i == 3 and int(s[start:start+i])>255:
                    return
                else:
                    sub_path += s[start:start+i] + '.'
                    backtracking_dfs(split_times+1,start+i,s,sub_path)
                    sub_path= sub_path[:-(1+i)]
        backtracking_dfs(0,0,s,"")
        return res