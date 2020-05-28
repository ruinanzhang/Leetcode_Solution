# Tag: Graph
# 344. Celebrity Problem
# -----------------------------------------------------------------------------------
# Description: 
# Given an binary matrix of N * N (the only elements in the matrix are 0s and 1s), each of the indices represents one person.
# matrix[i][j] = 1 if and only if person i knows person j (this is single direction, only if matrix[j][i] = 1 such that person j knows person i).
# Determine if there is one celebrity among all N persons, a celebrity is defined as:
#  "He does not know any other person. All the other persons know him."
# Return the celebrity's index if there exist one (there could be at most one celebrity, why?), return -1 otherwise.

# -----------------------------------------------------------------------------------
# Assumptions:
# The given matrix is not null and N >= 2.

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# 思路：
# Convert this problem to a graph problem: 
# If celebrity: indegree[i] >= n -1 (这个题有个bug；需要考虑matrix[i][i] = 1 or 0 两种情况)
# If celebrity: outdegree[i] ==0 or indegree[i] ==1 and matrix[i][i] = 1
# Traverse the matirx and keep two lists: indgree and outdegree 
# 最后加判别条件就好
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
class Solution(object):
  def celebrity(self, matrix):
    """
    input: int[][] matrix
    return: int
    """
    # write your solution here
    n = len(matrix)
    indeg = []
    outdeg = []
    t = 0
    for t in range(n):
      indeg.append(0)
      outdeg.append(0)
    i = 0
    j = 0
    if n == 1:
      return 0
    for i in range(n):
      for j in range(n):
        if matrix[i][j]:
          outdeg[i] +=1
          indeg[j] +=1
    for i in range(n):
      if outdeg[i] == 0 or (outdeg[i] == 1 and matrix[i][i] == 1):
        if indeg[i] == n or (indeg[i] == n -1 and matrix[i][i] == 0) :
          return i
    return -1
