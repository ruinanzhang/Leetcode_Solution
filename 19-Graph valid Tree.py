# Tag: Graph
# 261. Graph Valid Tree
# -----------------------------------------------------------------------------------
# Description:
# Given n nodes labeled from 0 to n-1 and a list of undirected edges
# (each edge is a pair of nodes), write a function to check whether
# these edges make up a valid tree.

# -----------------------------------------------------------------------------------
# Assumptions:
# you can assume that no duplicate edges will appear in edges.
#  Since all edges are undirected,
# [0,1] is the same as [1,0] and thus will not appear together in edges.

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# 思路：是graph的版别条件：a：没有cycle b：fully connceted
# 1. 确定用dfs， compute Adjacency List:
# 2. 从root node 0 开始，有一个visted list，每visit 一个 append 一个
# 3. Function: graph 没有cycle如果每个node 的 adj list里 visited 过的 neighbor 就是parent
# 因为如果某node里的一个nei，被visited过，还不是这个node的paren，就说明有cycle了！！
# 4. 从0开始走完一遍，看visited list，如果len<n，就说明有node不能从root到，说明不是fully connect
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        def nocycle(adjlist, node, visited, parent):
            visited.append(node)
            for nei in adjlist[node]:
                if nei not in visited:
                    nocycle(adjlist, nei, visited, node)
                elif parent != nei:
                    return False
            return True

        # Firts creat adjlist:
        adjlist = {x: [] for x in range(n)}
        for i, j in edges:
            adjlist[i].append(j)
            adjlist[j].append(i)
        visited = []

        if nocycle(adjlist, 0, visited, -1):
            if len(visited) < n:
                return False
            return True
        return False
