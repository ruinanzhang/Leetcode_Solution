# Tag: Backtracking
# 267. Palindrome Permutation II
# -----------------------------------------------------------------------------------
# Description:
# Given a string s, return all the palindromic permutations (without duplicates) of it.
# Return an empty list if no palindromic permutation could be form.
# -----------------------------------------------------------------------------------
# Example:
# Example 1:

# Input: "aabb"
# Output: ["abba", "baab"]
# Example 2:

# Input: "abc"
# Output: []
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# 思路：
# BackTracking
# 分条件考虑 *——*
# 如果是palindrome，必须是
# 1. str+单独的char+str[::-1] => len(odd) == 1
# 2. str+""+str[::-1] => len(odd) == 0
# 所以重点！先用counter = collections.Counter(s) computer counter dict
# odd = [key for key, value in counter.items() if value % 2 != 0]
# 按照len odd来分情况1，2讨论， 如果3: len（odd）>1 => return []
# backtrakcing pass in half_path, when len(half_path) == n//2 
# res.append + return
# operation: for every key in counters, 看一遍，如果val >0 and val%2 ==0
# path+key
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

class Solution:
    def generatePalindromes(self, s: str) -> List[str]:
        n = len(s)
        counter = collections.Counter(s)
        res = []
        odd = [key for key, value in counter.items() if value % 2 != 0]
        l = 2
        if len(odd)>1:
            return []
       
        def get_half_perm(path):
            if len(path) == n//2:
                res.append(path)
                return
            for key, values in counter.items():
                if values % 2 == 0 and values > 0:
                   counter[key] -=2
                   get_half_perm(path+key)
                   counter[key] +=2
                else:
                    continue
        if len(odd) == 1:  
            counter[odd[0]] -=1
        get_half_perm("")
        
        for ind in range(len(res)):
            if len(odd) == 1:
                res[ind] = res[ind]+odd[0]+res[ind][::-1]
            if len(odd) == 0:
                res[ind] = res[ind]+res[ind][::-1]
        return res

                
            