# Tag: Graph 
# 269. Alien Dictionary(Leetcode)
# -----------------------------------------------------------------------------------
# Description:
# There is a new alien language which uses the latin alphabet. 
# However, the order among letters are unknown to you.
# You receive a list of non-empty words from the dictionary, 
# where words are sorted lexicographically by the rules of this new language.
#  Derive the order of letters in this language.

# -----------------------------------------------------------------------------------
# Example:
# Input:
# [
#   "wrt",
#   "wrf",
#   "er",
#   "ett",
#   "rftt"
# ]

# Output: "wertf"
# -----------------------------------------------------------------------------------
# Assumptions: 
# You may assume all letters are in lowercase.
# If the order is invalid, return an empty string.
# There may be multiple valid order of letters, return any one of them is fine.
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# 思路：graph + topologival sort
# 1. 找到dependency 放到graph 的adjlist里
# for i in range(len(words)):
    # w1, w2 = words[i], words[i+1]
    # found = False ->立个flag，看有没有找到不一样的letter
    # 划重点！！我们只看相邻两个词之间的关系
    # min_len = min(len(w1),len(w2)) -> 在两个词里面找到length小的一个词，因为超过len的也不用比了
    # for j in range(min_len):
    #  if w1[j] != w2[j]: -> 如果这俩词有不同的letter，那说明w1[j]应该在w2[j]前面
    #   found = True
    #   在indegree adj list 里，inadj[w2[j]].append(w1[j])
    #   在outdegree adj list 里，inadj[w1[j]].append(w2[j])
    #   有两个list是因为topological sort里面要用到
    # if found = False and len(w1)>len(w2): ->!!!重点，如果没有找到不同的字母，w1还比w2长，
    # 说明不vaild 因为在字典里 "a" should be before "ab"
        # return ""
#　2. 有了adjlist，就可以去topological sort了，算法基本和之前20的一样： 
#  先找到没有indegree 的所有vertex，放到ZeroIndgreeList，
#  然后init sorted List L=[]
#  如果not ZeroIndgreeList：
        #return "" -> 说明没有起点
#  while ZeroIndgreeList:
#      node = ZeroIndgreeList.pop(0)
#      L.append(node)
#      for nei in outdegreeAdjlist[node]:
#           remove node from indegAdjlist[nei]
        #   if indegAdjlist[nei] is empty:
        #   ZeroIndgreeList.append(nei)
#   最后如果不是所有letter都在list L里，说明order不valid，return ”“ 
#   Return char in L in a string 
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
class Solution:
    def alienOrder(self, words: List[str]) -> str:
        #First, generate the directed adjlist structure for all letters
        if not words:
            return ""
        letterList = []
        for word in words:
            for letter in word:
                if letter not in letterList:
                    letterList.append(letter)
        inadjlist = {x:[] for x in letterList}
        outadjlist = {x:[] for x in letterList}
        #Second, put letters as vertices into adjlist
        for i in range(len(words)-1):
            w1, w2 = words[i], words[i+1]
            min_length = min(len(w1), len(w2))
            found = False
            for i in range(min_length):
                if w1[i] != w2[i]:
                    inadjlist[w2[i]].append(w1[i])
                    outadjlist[w1[i]].append(w2[i])
                    found = True
                    break 
            if found == False and len(w1) > len(w2):
                return ""
        # Thrid, Topological srot the adjlist 
        # Have a set with no in-degree: 
        zeroIndSet = []
        for v in inadjlist:
            if not inadjlist[v]:
                zeroIndSet.append(v)
        if not zeroIndSet:
            return ""
        temp = []
        while zeroIndSet:
            curr = zeroIndSet.pop(0)
            temp.append(curr)
            for nei in outadjlist[curr]:
                inadjlist[nei].remove(curr)
                if not inadjlist[nei]:
                    zeroIndSet.append(nei)
        if len(temp) < len(letterList):
            return ""         
        return "".join(temp)

            
        
                
                
        
        