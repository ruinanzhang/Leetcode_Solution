# Tag: Graph + Binary Tree + Recusion 
# 543. Diameter of Binary Tree(Leetcode)
# -----------------------------------------------------------------------------------
# Description:
# Given a binary tree, you need to compute the length of the diameter of the tree. 
# The diameter of a binary tree is the length of the longest path between 
# any two nodes in a tree. This path may or may not pass through the root.

# -----------------------------------------------------------------------------------
# Assumptions:
#The length of path between two nodes is represented by the number of edges between them.
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# 思路：Recurison+DFS
# 两种可能，从root开始的左右depht相加，或者在同一个subtree 里面的某个左右depht相加
# 要找最长pathway，用recursion的思维做：
# 1. 如果我们知道在每个subtree root node的 Left max Height and Right Height and Maxsum of 
# and 到此node为止的Maxsum = LeftmaxHeight + RightMaxHeight 
# 2. 我们就知道parent node 的 LeftmaxHeight, RightMaxHeight and Maxsum
# 3. Base case: if not root:
#                   return 0
# -----------------------------------------------------------------------------------
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        # Traverse from root to the leaf record the two 
        def maxHeight(root,maxsum):
            LmaxHeight = 0 
            RmaxHeight = 0
            if not root:
                return 0
            
            if root.left:
                LmaxHeight,maxsum = maxHeight(root.left,maxsum)
            if root.right: 
                RmaxHeight,maxsum =  maxHeight(root.right,maxsum)
            if LmaxHeight + RmaxHeight >= maxsum:
                maxsum = LmaxHeight + RmaxHeight
            if LmaxHeight>= RmaxHeight:
                return LmaxHeight + 1,maxsum
            if LmaxHeight< RmaxHeight:
                return RmaxHeight + 1,maxsum
                
        Lsubheight = 0
        Rsubheight = 0
        maxsum = 0
        if not root:
            return 0
        if root.left:
            Lsubheight,maxsum = maxHeight(root.left,maxsum)
        if root.right:
            Rsubheight,maxsum = maxHeight(root.right,maxsum)
        LRsum = Lsubheight + Rsubheight 
        if LRsum >= maxsum:
            return LRsum
        else:
            return maxsum