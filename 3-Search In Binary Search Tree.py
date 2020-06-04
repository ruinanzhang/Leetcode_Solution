# Tag : Binary Search Tree
# 52. Search In Binary Search Tree
# -----------------------------------------------------------------------------------
# Description:
# Find the target key K in the given binary search tree, 
# return the node that contains the key if K is found, otherwise return null.

# -----------------------------------------------------------------------------------
# Assumptions:
# There are no duplicate keys in the binary search tree

#  -----------------------------------------------------------------------------------
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# *************************************************************************************
# Solution: 

# Very similar to Insert In Binary Search Tree
class Solution(object):
  def search(self, root, key):
    """
    input: TreeNode root, int key
    return: TreeNode
    """
    if root == None: 
      return None

    if root.val == key :
      return root

    else: 
      if root.val > key:
        if root.left is None: 
          return None
        else:
          return Solution.search(self, root.left, key)
      if root.val < key: 
        if root.right is None:
          return None
        else: 
          return Solution.search(self, root.right, key)