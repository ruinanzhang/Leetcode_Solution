# Tag: Graph
# 219. Disjoint White Objects
# -----------------------------------------------------------------------------------
# Description:
# In a 2D black image there are some disjoint white objects with arbitrary shapes,
# find the number of disjoint white objects in an efficient way.

# By disjoint, it means there is no white pixels that can connect the two objects,
# there are four directions to move to a neighbor pixel (left, right, up, down).

# Black is represented by 1’s and white is represented by 0’s.

# -----------------------------------------------------------------------------------
# Assumptions:
# The given image is represented by a integer matrix and all the values in the matrix are 0 or 1
# The given matrix is not null
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# 思路：还是得找到adj list
# 但这个adj list比较好找是因为只用看上下左右4个node
# if ==1, 直接pass
# Then dfs on adj list using a falg seen[]
# if not seen and matrix value ==0:
# count ++
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


class Solution(object):
    def whiteObjects(self, matrix):
        """
        input: int[][] matrix
        return: int
        """
        def find_adj(matrix):
            row = len(matrix)
            col = len(matrix[0])
            res = {x: [] for x in range(row*col)}
            curr = 0
            arr = {}
            for i in range(row):
                for j in range(col):
                    # 如果是1，直接+1 pass
                    if matrix[i][j] == 1:
                        arr[curr] = 1
                        curr += 1
                    # if ==0, calculate adj list:
                    if matrix[i][j] == 0:
                        if i+1 <= row-1:
                            if matrix[i+1][j] == 0:
                                res[curr].append(curr+col)
                        if j+1 <= col-1:
                            if matrix[i][j+1] == 0:
                                res[curr].append(curr+1)
                        if i-1 >= 0:
                            if matrix[i-1][j] == 0:
                                res[curr].append(curr-col)
                        if j-1 >= 0:
                            if matrix[i][j-1] == 0:
                                res[curr].append(curr-1)
                        arr[curr] = 0
                        curr += 1
            return res, arr

        seen = []
        row = len(matrix)
        col = len(matrix[0])
        count = 0

        def dfs(i, adj_list, seen):
            if i not in seen:
                seen.append(i)
                for nei in adj_list[i]:
                    dfs(nei, adj_list, seen)

        adj_list, arr = find_adj(matrix)
        for i in range(row*col):
            if i not in seen and arr[i] == 0:
                count += 1
                dfs(i, adj_list, seen)
        return count
