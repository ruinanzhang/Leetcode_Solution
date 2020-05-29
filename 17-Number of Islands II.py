# Tag: Graph
# 305. Number of Islands II(LEETCODE)
# -----------------------------------------------------------------------------------
# Description:
# A 2d grid map of m rows and n columns is initially filled with water. 
# We may perform an addLand operation which turns the water at position (row, col) into a land. 
# Given a list of positions to operate, count the number of islands after each addLand operation. 
# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 
# You may assume all four edges of the grid are all surrounded by water.
# -----------------------------------------------------------------------------------
# Assumptions:
# N/A
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# 思路：还是用16用的Union-Find思路
# Poisions里的每个operations都算一遍
# 每个op in Poisions：[i,j]
# 1. 看看 if matrix[i,j] == 0, if ==1 -> pass (已经见过了)
# 2. if matrix[i,j] == 0 -> count ++
# 3. matrix[i][j] = 1 把matrix里的0换成1
# 4.上下左右看一下matrix，如果附近有1就给union find一下，count--

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        
        def find(x):
            if parent[x]!=x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x,y,count):
            xroot,yroot = find(x),find(y)
            if xroot == yroot:
                return count
            parent[xroot] = yroot
            return (count-1)
        
        if m*n ==0:
            return 0
        count = 0
        res = []
        parent = [i for i in range(m*n)]
        matrix = [ [0 for i in range(n)] for j in range(m)] 
        for op in range(len(positions)):
            i, j = positions[op]
            if matrix[i][j]== 0:
                count +=1
                matrix[i][j] = 1
                index = i*n+j
                if i-1>=0 and matrix[i-1][j] == 1:
                    count =union(index,index-n,count)
                if j-1>=0 and matrix[i][j-1] == 1:
                    count =union(index,index-1,count)
                if i<m-1 and matrix[i+1][j] == 1:
                    count =union(index,index+n,count)
                if j<n-1 and matrix[i][j+1] == 1:
                    count =union(index,index+1,count)
                    
            res.append(count)
        return res
        
