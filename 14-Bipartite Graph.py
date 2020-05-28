# Tag: Graph
# 785. Is Graph Bipartite? (Leetcode)
# -----------------------------------------------------------------------------------
# Description: 
# Given an undirected graph, return true if and only if it is bipartite.

# Recall that a graph is bipartite if we can split it's set of nodes into two independent 
# subsets A and B such that every edge in the graph has one node in A and another node in B.

# The graph is given in the following form: graph[i] is a list of indexes j for which the 
# edge between nodes i and j exists.  Each node is an integer between 0 and graph.length - 1. 
#  
# There are no self edges or parallel edges: graph[i] does not contain i, and it doesn't contain 
# any element twice.

# -----------------------------------------------------------------------------------
# Assumptions:
# N/A
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# 思路：
# DFS + Color 
# 在dfs traverse整个graph的同时，use a color list to record each node's color 
# If no neighbor nodes have same color, then the graph is bipartite. 
# 1. For every node in the graph: 注意每个node都要看一遍因为可能有的node是完全孤立的，
# color it if not colored 
# 2. run dfs on that node, and recusively check every neighbors in that
# node's adj list, 如果有一样的color-> return FALSE
# 3. 如果这个nei没有被color过，color it and then run dfs on it untill 这条path上的
# 点都被color过了
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        def dfs(node):
            for nei in graph[node]:
                if nei in color: 
                    if color[nei] == color[node]:
                        return False
                else:
                    color[nei] = 1 - color[node]
                    if not dfs(nei):
                        return False
            return True
        color = {}
        for i in range(len(graph)):
            if i not in color:
                color[i] = 0
                if not dfs(i):
                    return False
        return True