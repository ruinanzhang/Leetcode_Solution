# Tag: Graph
# 457.Number of Connected Components in an Undirected Graph
# -----------------------------------------------------------------------------------
# Description: 
# Given n nodes labeled from 0 to n - 1 and a list of undirected edges 
# (each edge is a pair of nodes), write a function to find the number of connected components 
# in an undirected graph.

# -----------------------------------------------------------------------------------
# Assumptions:
# N/A
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# 思路：
# DFS 
# 1. First, build adjacency list: 
# g = {x:[] for x in range(n)}
# For u,v in edges: 
#   g[u].append(v)
#   g[v].append(u)
# 2. DFS using adjacency list -> seen[]
# 见过的node放到seen里，recursively dfs(node的neighbor using adj list)--> 直到都是seen，
# 这个时候已经没有可以从这个node任何一个edge到的点了，
# 3. 换到另一个node，条件是 if node not in seen 
# 4. Have a counter, everytime change node, count++
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
class Solution(object):
  def countComponents(self, n, edges):
    """
    input: int n, int[][] edges
    return: int
    """
    seen = []
    g = {x:[] for x in range(n)}
    count = 0 
    for u, v in edges:
      g[u].append(v)
      g[v].append(u)
    for i in range(n):
      if i not in seen:
        count+=1
        dfs(i,seen,g)
    return count 
def dfs(node,seen,g):
  if node not in seen:
    seen.append(node)
    for adjnode in g[node]:
      dfs(adjnode,seen,g)