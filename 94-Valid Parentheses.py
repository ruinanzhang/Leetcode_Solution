# Tag: Stack
# 20. Valid Parentheses
# -----------------------------------------------------------------------------------
# Description: 

# Given a string containing just the characters '(', ')', '{', '}', '[' and ']',
# determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.

# Note：
# that an empty string is also considered valid.
# -----------------------------------------------------------------------------------
#Example 1:
# Input: "()"
# Output: true

# Example 2:

# Input: "()[]{}"
# Output: true
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# 思路：
# 用stack，open放进去，close pop出来
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
class Solution:
    def isValid(self, s: str) -> bool:
        open_list = ["{","[","("]
        open_stack = []
        close_stack = []
        for char in s:
            if char in open_list:
                open_stack.append(char)
            if not open_stack:
                return False
            if char == "}":
                last_open = open_stack.pop()
                if last_open != "{":
                    return False 
            if char == "]":
                last_open = open_stack.pop()
                if last_open != "[":
                    return False
            if char == ")":
                last_open = open_stack.pop()
                if last_open != "(":
                    return False 
        if open_stack:
            return False
        return True
        