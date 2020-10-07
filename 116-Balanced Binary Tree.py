# Tag: BST
# 110. Balanced Binary Tree
# -----------------------------------------------------------------------------------
# Description:
# Given a binary tree, determine if it is height-balanced.
# For this problem, a height-balanced binary tree is defined as:
# a binary tree in which the left and right subtrees of every node differ in height by no more than 1.
# -----------------------------------------------------------------------------------
# Example 1:
# Input: root = [1,2,2,3,3,null,null,4,4]
# Output: false
# -----------------------------------------------------------------------------------
# Constraints:
# The number of nodes in the tree is in the range [0, 5000].
# -104 <= Node.val <= 104
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# 思路: Recursion Top-down
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Check recursively, if valid left-sub and valid right-sub : valid
# **** This is top-down nlogn
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True
        return (abs(self.get_height(root.left) - self.get_height(root.right)) <=1) and self.isBalanced(root.left) and self.isBalanced(root.right)
    def get_height(self,root):
        if not root:
            return 0
        h = max(self.get_height(root.left), self.get_height(root.right))+1
        return h
# **** this is bottom-up,check if balanced while recursion, pass in height 
# class Solution:
    # Return whether or not the tree at root is balanced while also returning
    # the tree's height
    def isBalancedHelper(self, root: TreeNode) -> (bool, int):
        # An empty tree is balanced and has height -1
        if not root:
            return True, -1
        
        # Check subtrees to see if they are balanced. 
        leftIsBalanced, leftHeight = self.isBalancedHelper(root.left)
        if not leftIsBalanced:
            return False, 0
        rightIsBalanced, rightHeight = self.isBalancedHelper(root.right)
        if not rightIsBalanced:
            return False, 0
        
        # If the subtrees are balanced, check if the current tree is balanced
        # using their height
        return (abs(leftHeight - rightHeight) < 2), 1 + max(leftHeight, rightHeight)
        
    def isBalanced(self, root: TreeNode) -> bool:
        return self.isBalancedHelper(root)[0]      
    