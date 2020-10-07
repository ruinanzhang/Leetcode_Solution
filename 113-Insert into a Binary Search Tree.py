# Tag: BST
# 701. Insert into a Binary Search Tree
# -----------------------------------------------------------------------------------
# Description:
# Given the root node of a binary search tree (BST) and a value to be inserted into 
# the tree, insert the value into the BST. Return the root node of the BST after the 
# insertion. It is guaranteed that the new value does not exist in the original BST.

# Note that there may exist multiple valid ways for the insertion, as long as the tree 
# remains a BST after insertion. You can return any of them.
# -----------------------------------------------------------------------------------
# For example, 
# Given the tree:
#         4
#        / \
#       2   7
#      / \
#     1   3
# And the value to insert: 5
# You can return this binary search tree:
#          4
#        /   \
#       2     7
#      / \   /
#     1   3 5
# -----------------------------------------------------------------------------------
# Constraints:
# The number of nodes in the given tree will be between 0 and 10^4.
# Each node will have a unique integer value from 0 to -10^8, inclusive.
# -10^8 <= val <= 10^8
# It's guaranteed that val does not exist in the original BST.
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# 思路: Recursion
# If root is null - return TreeNode(val).
# If val > root.val - go to insert into the right subtree.
# If val < root.val - go to insert into the left subtree.
# Return root.
# BST INSERT / FIND TIME O(LOGn)->0(h)
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        def helper(root,val):
            if not root:
                return TreeNode(val)
            if root.val < val:
                root.right = helper(root.right,val)
            else:
                root.left = helper(root.left,val)
            return root
        return helper(root,val)