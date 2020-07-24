# Tag: Sliding Window + stack
# 3. Longest Substring Without Repeating Characters
# -----------------------------------------------------------------------------------
# Description:
# Given a string, find the length of the longest substring without repeating characters.
# -----------------------------------------------------------------------------------
# Example:
#Example 1:
# Input: "abcabcbb"
# Output: 3 
# Explanation: The answer is "abc", with the length of 3. 

# Example 2:
# Input: "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# -----------------------------------------------------------------------------------
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#   这种找最长subarray/str的->sliding window+hash map
#   因为这里每个map里的数肯定是unique的，所以考虑用stack
#   每次找到repeat num 不用从头开始，->stack[prev_repeat_ind+1:]
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        max_len = 0
        prev_repeat_ind = 0
        stack = []
        for index,char in enumerate(s):
            if char not in stack:
                stack.append(char)
                if len(stack) > max_len:
                    max_len = len(stack)
            elif char in stack:
                prev_repeat_ind = stack.index(char)
                if len(stack) > max_len:
                    max_len = len(stack)
                stack = stack[prev_repeat_ind+1:]
                stack.append(char)

        return max_len