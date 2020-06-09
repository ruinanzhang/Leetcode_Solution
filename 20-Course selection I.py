# Tag: Graph
# 207. Course Schedule (LeetCode)
# -----------------------------------------------------------------------------------
# Description:
# There are a total of numCourses courses you have to take, labeled from 0 to numCourses-1.

# Some courses may have prerequisites, for example to take course 0 you have to first
# take course 1, which is expressed as a pair: [0,1]

# Given the total number of courses and a list of prerequisite pairs,
# is it possible for you to finish all courses?

# -----------------------------------------------------------------------------------
# Assumptions:
# The input prerequisites is a graph represented by a list of edges,
#  not adjacency matrices. Read more about how a graph is represented.
# You may assume that there are no duplicate edges in the input prerequisites.
# 1 <= numCourses <= 10^5

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# 思路：Topological Sort
# 1. Empty List L, NoIndegree Set S
# 2. Compute Indegree Adj list and OutDegree AdjList
# 3. 找到没有indegree的node，放到NoIndegree Set S里
# 4. While Set S is not emopty:
# 5.    remove node n from S
# 6.    add n to list L
# 7.    For neighbors(nei m) in the OutDegree Adjlist of node n:
# 8.        Remove node n from nei m's Indegree Adjlist
# 9.        if nei m's Indegree list is empty:
# 10.           add m to set S
# 11. If List L's 的size 比 number of nodes 小， 说明有node不能topological sort
# 12.Return False then
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # First compute indegree adjlist:
        Inlist = {x: []for x in range(numCourses)}
        Outlist = {x: []for x in range(numCourses)}
        L = []
        for i, j in prerequisites:
            Inlist[i].append(j)
            Outlist[j].append(i)
        noInset = []
        for x in Inlist:
            if len(Inlist[x]) == 0:
                noInset.append(x)
        if not noInset:
            return False
        while noInset:
            node = noInset.pop(0)
            L.append(node)
            for nei in Outlist[node]:
                Inlist[nei].remove(node)
                if not Inlist[nei]:
                    noInset.append(nei)

        if len(L) == numCourses:
            return True
        return False

# Alternative DFS solution:


def canFinish(self, numCourses, prerequisites):
    graph = [[] for _ in xrange(numCourses)]
    visit = [0 for _ in xrange(numCourses)]
    for x, y in prerequisites:
        graph[x].append(y)

    def dfs(i):
        if visit[i] == -1:
            return False
        if visit[i] == 1:
            return True
        visit[i] = -1
        for j in graph[i]:
            if not dfs(j):
                return False
        visit[i] = 1
        return True
    for i in xrange(numCourses):
        if not dfs(i):
            return False
    return True
