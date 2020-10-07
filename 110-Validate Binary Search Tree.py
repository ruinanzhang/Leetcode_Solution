# Tag: BST
# 98. Validate Binary Search Tree
# -----------------------------------------------------------------------------------
# Description:
# Given a binary tree, determine if it is a valid binary search tree (BST).

# Assume a BST is defined as follows:
# The left subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.
# -----------------------------------------------------------------------------------
# Examples:
# Example 1:

#     2
#    / \
#   1   3

# Input: [2,1,3]
# Output: true
# Example 2:

#     5
#    / \
#   1   4
#      / \
#     3   6

# Input: [5,1,4,null,null,3,6]
# Output: false
# Explanation: The root node's value is 5 but its right child's value is 4.
# -----------------------------------------------------------------------------------
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# 思路 1：
# Inorder Traverse: 
# global prev， flag
# 如果 traverse 的每一个node val 都比之前的小就ok，如果大，set global flag false
# return flag
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        self.prev = float('-inf')
        self.flag = True
        def recursion(root):
            if not root:
                return 
            recursion(root.left)
            value = root.val 
            if value <= self.prev:
                self.flag = False
            self.prev = value
            recursion(root.right)
        recursion(root)
        return self.flag
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# 思路 2：
# Use Recursion: 
# If we know left is valid and right is valid -> we know curr is valid 
# base case: not root -> True 
# valid condition: curr value < min and curr value > max
# if go left: update 
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
class Solution:
    # Use Recursion: 
    # If we know left is valid and right is valid -> we know curr is valid 
    # base case: not root -> True 
    def isValidBST(self, root: TreeNode) -> bool:
        def recursion(root,min,max):
            if not root:
                return True
            if root.val <= min or root.val >= max:
                return False 
            else:
                return recursion(root.left,min,root.val) and recursion(root.right,root.val,max)
        min = float('-inf')
        max = float('inf')
        return recursion(root,min,max)