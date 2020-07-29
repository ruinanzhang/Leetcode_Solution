# Tag: Sliding Window! Hardddd
# 76. Minimum Window Substring
# -----------------------------------------------------------------------------------
# Description:
# Given a string S and a string T, find the minimum window in S which will contain
# all the characters in T in complexity O(n).
# -----------------------------------------------------------------------------------
# Example:
# Input: S = "ADOBECODEBANC", T = "ABC"
# Output: "BANC"
# -----------------------------------------------------------------------------------
# Note: 
# If there is no such window in S that covers all characters in T, return the empty string "".
# If there is such window, you are guaranteed that there will always be only one unique minimum window in S.
# -----------------------------------------------------------------------------------
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# 思路:
# Sliding window(hash map + two pointer)
# 首先要注意这个题可能有重复！！！
# 2 ptrs: start, right -> init start = 0 ; end = 0
# global vars: min_start; min_sub_len
# 还需要准备一个hashmap: freq_dict_t {} 这个map记录target里面的char和他们的frequency
# if t = “ABC" freq_dict_t = {A:1,B:1,C:1}
# unique_num_to_be_found = len(t) 有多少个unique的char需要我们找
# filled = 0 已经找到了几个char
# 1. 整体思路：end pointer moving towards the end of the input string 
# - > if s[end] in freq_dict_t: 
#       freq_dict_t[s[end]]-=1
# ->  if freq_dict_t[s[end]] == 0
#       filled +=1 ！！！重点，因为可能有重复，必须要freq_dict_t此char对应的frequency都找到了filled才能+1
# -> while filled == unique_num_to_be_found: (if we already found all chars in this sub_string):
#       update golbal min_start and min_sub_len
#       这个时候我们从这个sub string的最开头excludechar：
#       if s[start] in freq_dict_t: if this char is one of the chars we are looking for:
#           freq_dict_t[s[start]]+=1
#           if freq_dict_t[s[start]]>0 如果这个时候发现我们又需要找这个数了：
#           filled -=1
#       start +=1
    # end +=1
# 2. corner case: 因为如果只有一个char，最小的sub_str就是len(s) 所以初始值min_sub_str = len(s)+1
#  if at the every end it's still len(s)+1 -> return ""
#  else: return min_sub_str

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        start = end = 0
        min_sub_start = 0
        min_sub_len = len(s) +1
        freq_dict_t = {}
        for char in t:
            if char not in freq_dict_t:
                freq_dict_t[char] = 1
            else:
                freq_dict_t[char] += 1
        uniqe_num_to_be_filled = len(freq_dict_t)
        filled = 0

        while end<len(s):
            curr = s[end]
            if curr in freq_dict_t:
                freq_dict_t[curr]-=1        
                if freq_dict_t[curr] == 0:
                    filled +=1
            while filled == uniqe_num_to_be_filled:
                curr_sub_len = end - start + 1
                if curr_sub_len < min_sub_len:
                    min_start = start
                    min_sub_len = curr_sub_len
                num_to_be_remove = s[start]
                if num_to_be_remove in freq_dict_t:
                    freq_dict_t[num_to_be_remove]+=1
                    if freq_dict_t[num_to_be_remove]>0:
                        filled -=1
                
                start +=1
            end +=1
        if min_sub_len == len(s)+1:
            return ""
        return s[min_start:min_start+min_sub_len]

