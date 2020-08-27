# Tag: String + Array 
# 165. Compare Version Numbers
# -----------------------------------------------------------------------------------
# Description: 

# Compare two version numbers version1 and version2.
# If version1 > version2 return 1; if version1 < version2 return -1;otherwise return 0.
# You may assume that the version strings are non-empty and contain only digits and the . character.
# The . character does not represent a decimal point and is used to separate number sequences.
# For instance, 2.5 is not "two and a half" or "half way to version three", it is the fifth
#  second-level revision of the second first-level revision.
# You may assume the default revision number for each level of a version number to be 0. For example,
# version number 3.4 has a revision number of 3 and 4 for its first and second level revision number. Its third and fourth level revision number are both 0.
# -----------------------------------------------------------------------------------
# Note:

# Only constant extra memory is allowed.
# You may not alter the values in the list's nodes, only nodes itself may be changed.
# -----------------------------------------------------------------------------------
# Example 1:

# Input: version1 = "0.1", version2 = "1.1"
# Output: -1

# Example 2:

# Input: version1 = "1.0.1", version2 = "1"
# Output: 1
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# 思路：
# Split by "." -> 2 lists, 用零补齐，每一个item的对比
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1_list =  version1.split(".")
        v2_list =  version2.split(".")
        l1 = len(v1_list)
        l2 = len(v2_list)
        while l1>l2:
            v2_list.append("0")
            l2 +=1
        while l2>l1:
            v1_list.append("0")
            l1+=1
        res = 0
        for i in range(len(v1_list)):
            if int(v1_list[i]) > int(v2_list[i]):
                return 1
            elif int(v1_list[i]) < int(v2_list[i]):
                return -1
        return 0