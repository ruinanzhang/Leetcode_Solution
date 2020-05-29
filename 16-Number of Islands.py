# Tag: Graph
# 200. Number of Islands
# -----------------------------------------------------------------------------------
# Description:
# Given a 2d grid map of '1's (land) and '0's (water), count the number of islands.
# An island is surrounded by water and is formed by connecting adjacent lands
# horizontally or vertically. You may assume all four edges of the grid are
# all surrounded by water.
# -----------------------------------------------------------------------------------
# Assumptions:
# N/A
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# 思路：虽然可以用15类似的思路先算adj list然后 dfs
# 这题用union find更简单
# 1. count所有grid[i][j] == 1
# 2. for all gird[i][j] ==1 看一下 ➡️ 和 ⬇ 的 点是不是1，如果是1就union
# 3. 每union一个点，count --
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def find(x):
            # 如果x's parent is not itself:
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y, count):
            x_parent = find(x)
            y_parent = find(y)
            # X,Y已经在一个set了，啥也不干.count不多也不少
            if x_parent == y_parent:
                return count
            # X，Y不在一个set，x's parent 指向y parent，count -1
            # 这里-1是因为union了几次就少了几个孤岛啊
            parent[x_parent] = y_parent
            return count - 1
        if len(grid) == 0:
            return 0
        count = 0
        row = len(grid)
        col = len(grid[0])
        # let all points' parent be themselves:

        parent = [i for i in range(row*col)]
        # 计算一下有几个1
        for i in range(row):
            for j in range(col):
                if grid[i][j] == '1':
                    count += 1
        for i in range(row):
            for j in range(col):
                index = i*col + j
                if grid[i][j] == '0':
                    continue
                if grid[i][j] == '1':
                    if i < row-1 and grid[i+1][j] == '1':
                        count = union(index, index+col, count)
                    if j < col - 1 and grid[i][j+1] == '1':
                        count = union(index, index+1, count)
        return count
