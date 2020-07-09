# Tag: BST
# 662. Maximum Width of Binary Tree
# -----------------------------------------------------------------------------------
# Description:
# Given a binary tree, write a function to get the maximum width of the given tree. 
# The width of a tree is the maximum width among all levels. The binary tree has the same 
# structure as a full binary tree, but some nodes are null.
# The width of one level is defined as the length between the end-nodes 
# (the leftmost and right most non-null nodes in the level, 
# where the null nodes between the end-nodes are also counted into the length calculation.
# -----------------------------------------------------------------------------------
# Example:
# Input: 

#            1
#          /   \
#         3     2
#        / \     \  
#       5   3     9 

# Output: 4
# Explanation: The maximum width existing in the third level with the length 4 (5,3,null,9).
# -----------------------------------------------------------------------------------
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# 思路：
#       重点在于keep track of node 的 position:
#       用一个table记录每层最开始的node的index，然后每次scan每个node：
#       找到curr node 的index和每层最开始的node的index的差的与global的max
#       update global max
#       max(self.res, index - start[level] + 1)
#       if node ind= i then:
#       then node.left ind = 2*i
#       node.right ind = 2*i+1
#       also have a global max_width to compare with
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
#       init global max_width
        self.res = 1
        self.dfs(root, 0, 1, [])
        return res

    def dfs(self, root, level, index, start):
        if not root: return 
        
        if len(start) == level:
            start.append(index)
        else:
            self.res = max(self.res, index - start[level] + 1)
        self.dfs(root.left, level + 1, index * 2, start)
        self.dfs(root.right, level + 1, index * 2 + 1, start)
        

            
        
            
            
            

        
        