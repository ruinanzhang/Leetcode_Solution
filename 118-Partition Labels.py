# Tag: BST
# 763. Partition Labels
# -----------------------------------------------------------------------------------
# Description:
# A string S of lowercase English letters is given. We want to partition this string 
# into as many parts as possible so that each letter appears in at most one part, and 
# return a list of integers representing the size of these parts.
# -----------------------------------------------------------------------------------
# Example 1:

# Input: S = "ababcbacadefegdehijhklij"
# Output: [9,7,8]
# Explanation:
# The partition is "ababcbaca", "defegde", "hijhklij".
# This is a partition so that each letter appears in at most one part.
# A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.
# -----------------------------------------------------------------------------------
# Note:
# S will have length in range [1, 500].
# S will consist of lowercase English letters ('a' to 'z') only.
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# 思路: put in map, get each word's interval 
# 三种情况
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        N = len(S)
        map = {}
        for i in range(len(S)):
            if S[i] not in map:
                map[S[i]] = [i]
            else: 
                if len(map[S[i]]) > 1:
                    map[S[i]][1] = i
                else:
                     map[S[i]].append(i)
        k = 1
        count = 0
        stack = []
        for key, value in map.items():
            if not stack:
                stack.append(value)
            else:
                if len(stack[-1]) == 1:
                    prev_end = stack[-1][0]
                else:
                    prev_end = stack[-1][1]
                #no overlap:
                if value[0] > prev_end:
                    stack.append(value)
                #full overlap:
                if len(value) == 1 and value[0] < prev_end:
                    continue
                if len(value) > 1 and value[1]<prev_end:
                    continue
                elif value[0] < prev_end and value[1]>prev_end:
                    stack[-1][1] = value[1]
        res = []
        for interval in stack:
            if len(interval) == 1:
                res.append(1)
            else:
                res.append(interval[1]- interval[0]+1)
            
            
        return res
                
        