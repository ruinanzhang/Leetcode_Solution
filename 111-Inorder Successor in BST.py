# Tag: BST
# 285. Inorder Successor in BST
# -----------------------------------------------------------------------------------
# Description:
# Given a binary search tree and a node in it, find the in-order successor of 
# that node in the BST.

# The successor of a node p is the node with the smallest key greater than p.val.
# -----------------------------------------------------------------------------------
# Example 1:
# Input: root = [2,1,3], p = 1
# Output: 2
# Explanation: 1's in-order successor node is 2. Note that both p and the return value is of TreeNode type.
# -----------------------------------------------------------------------------------
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# 思路 1：
# Inorder Traverse: 
# global res, flag
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        self.isNext = False 
        self.res = None
        def inOrderTraverse(root,target):
            if not root:
                return 
            inOrderTraverse(root.left,target)
            if root.val == target.val:
                self.isNext = True
            if root.val != target.val and self.isNext:
                self.res = root
                self.isNext = False
            inOrderTraverse(root.right,target)
        inOrderTraverse(root,p)
        
        return self.res
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# 思路 2：
# Here is a much simpler solution to the problem. The idea is pretty straight forward.
# We start from the root, utilizing the property of BST:

# If current node's value is less than or equal to p's value, we know our answer must be in the right subtree.
# If current node's value is greater than p's value, current node is a candidate. Go to its left subtree to see if we can find a smaller one.
# If we reach null, our search is over, just return the candidate.
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        res = None 
        cur = root
        while cur:
            if cur.val > p.val:
                res = cur
                cur = cur.left
            else:
                cur = cur.right
        return res
                