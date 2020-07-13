# Tag: BST + RECURSION
# 100. Same Tree
# -----------------------------------------------------------------------------------
# Description:
# Given two binary trees, write a function to check if they are the same or not.
# Two binary trees are considered the same if they are structurally identical and the nodes have the same value.
# -----------------------------------------------------------------------------------
# Example:
# Input:     1         1
#           /           \
#          2             2

#         [1,2],     [1,null,2]

# Output: false
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# 思路：
# Recursion, return 这一步比较重要！！！
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
#       just traverse two trees at the same time and see if they have smae structure and value
        
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
       