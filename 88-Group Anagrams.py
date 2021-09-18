# Tag: Hash Table + String
# 49. Group Anagrams
# -----------------------------------------------------------------------------------
# Description: 

# Given an array of strings, group anagrams together.
# -----------------------------------------------------------------------------------
# Note:

# All inputs will be in lowercase.
# The order of your output does not matter.
# -----------------------------------------------------------------------------------
# Example:

# Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
# Output:
# [
#   ["ate","eat","tea"],
#   ["nat","tan"],
#   ["bat"]
# ]
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# 思路：
# For every string in input: 
# eg. "eat" -> sorted("eat") == ["a","e","t"] -> "".join(["a","e","t"])
# -> ["aet"]
# In this way, all strings consist of same chars will be have same key
# ** To iterate a dict: use for key, value in dict.items():
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        str_dict = {}
        result = []
        for string in strs:
            chars = sorted(string)
            key = "".join(chars)
            #if key in str_dict:
            #    str_dict[key].append(string)
            #else: 
            #    str_dict[key] = [string]
            # 一个优化：
            str_dict[key] = str_dict.get(key,[])+[string]
        for key, value in str_dict.items():
           result.append(value)
        return result

       