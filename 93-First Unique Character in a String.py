# Tag: Array + dict 
# 387. First Unique Character in a String
# -----------------------------------------------------------------------------------
# Description: 

# Given a string, find the first non-repeating character in it and return its index. 
# If it doesn't exist, return -1.
# -----------------------------------------------------------------------------------
# Note:
# You may assume the string contains only lowercase English letters.
# -----------------------------------------------------------------------------------
# Examples:

# s = "leetcode"
# return 0.

# s = "loveleetcode"
# return 2.
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# 思路：如果是统计s/list里面element的个数，直接用counter = collections.Counter(target)
# 统计完了iter list，第一个count=1的就是return的，如过没有，return-1
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
class Solution:
    def firstUniqChar(self, s: str) -> int:
        if not s:
            return -1
        n = len(s)
        # Use python's counter!!!!!!!!
        # my_map = {}
        # for index, value in enumerate(s):
            # if value not in my_map:
                # my_map[value] = [index]
            # else:
                # my_map[value].append(index)
        my_map = collections.Counter(s)
        for index,char in enumerate(s):
            if my_map[char] == 1:
                return index
        return -1