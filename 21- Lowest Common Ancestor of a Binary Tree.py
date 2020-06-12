# Tag: Graph
# 236. Lowest Common Ancestor of a Binary Tree(Leetcode)
# -----------------------------------------------------------------------------------
# Description:
# Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

# According to the definition of LCA on Wikipedia: “The lowest common 
# ancestor is defined between two nodes p and q as the lowest node in T that 
# has both p and q as descendants (where we allow a node to be a descendant of itself).”
# Given the following binary tree:  root = [3,5,1,6,2,0,8,null,null,7,4]

# -----------------------------------------------------------------------------------
# Assumptions:
# All of the nodes' values will be unique.
# p and q are different and both values will exist in the binary tree.
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# 思路：Recurison
# -----------------------------------------------------------------------------------
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        if root is None:
            return root
        if root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left, p , q)
        right = self.lowestCommonAncestor(root.right, p , q)
        if left and right:
            return root 
        if left and not right:
            return left
        if right and not left:
            return right
        