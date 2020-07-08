# Tag: String + Hash Map
# 266. Palindrome Permutation
# -----------------------------------------------------------------------------------
# Description:
# Given a string, determine if a permutation of the string could form a palindrome.
# -----------------------------------------------------------------------------------
# Example 1:
# Input: "code"
# Output: false
# -----------------------------------------------------------------------------------
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# 思路：
# if string s = "abbbs"
# Hash Map :{'a': 1, 's': 1, 'b': 3}
# 如果只有一个odd count 或没有 odd count -> can get palindromic permutation 
# otherwise: can't get permutation. 
# 👌👌👌 python hashmap
hashmap = {}
for char in s:
    if char not in hashmap:
        hashmap[char] =1
    if char in hashmap:
        hashmap[char]
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        n = len(s)
        if len(s) <=1:
            return True
        dic = {}
        for str in s:
            if str in dic:
                dic[str] += 1
            else:
                dic[str] = 1
        count = 0
        for key in dic:
            if dic[key] % 2 == 1:
                count += 1
        if count == 0 or count == 1:
            return True
        else:
            return False