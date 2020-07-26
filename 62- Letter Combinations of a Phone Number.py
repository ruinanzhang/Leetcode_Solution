# Tag: Recursion
# 17. Letter Combinations of a Phone Number
# -----------------------------------------------------------------------------------
# Description:
# Given a string containing digits from 2-9 inclusive, return all possible letter 
# combinations that the number could represent.

# A mapping of digit to letters (just like on the telephone buttons) is given below.
#  Note that 1 does not map to any letters.
# -----------------------------------------------------------------------------------
# Example:
# Input: "23"
# Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
# ]
# -----------------------------------------------------------------------------------
# Note: 
# Although the above answer is in lexicographical order, 
# your answer could be in any order you want.
# -----------------------------------------------------------------------------------
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# 思路：recursion
# sub-prob：如果知道digits[0:n-1]的letter comb,在排列组合上cur digit 的letter comb就能得出答案
# BASE CASE: len(digits) == 1: sol:["char_a","char_b","char_c"]
# RECURSIVE STEP: 
# if N > 0:
# sub_sol = recur(digits[:N-1])
#                 for s in sub_sol:
#                     for char in letter_map[int(digits[-1])]:
#                         sol.append(s + char)
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letter_map = {x:[] for x in range(1,10)}
        alpha_str = 'abcdefghijklmnopqrstuvwxyz'
        start = 0
        for x in letter_map:
            if x == 1 :
                continue
            if x == 7 or x ==9:
                letter_map[x] = (alpha_str[start:start+4])
                start = start+4
            else: 
                letter_map[x] = (alpha_str[start:start+3])
                start = start+3
        
        def recur(digits):
#           Base case
            if len(digits) == 1:
                d = digits[0]
                letters = letter_map[int(d)]
                sol = []
                for char in letters:
                    sol.append(char)
                return sol
#           recursive step:
            sol = []
            N = len(digits)
            if N >0:
                sub_sol = recur(digits[:N-1])
                for s in sub_sol:
                    for char in letter_map[int(digits[-1])]:
                        sol.append(s + char)
            return sol
        return recur(digits)
        
                        

            