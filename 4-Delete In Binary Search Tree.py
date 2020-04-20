# Tag : Binary Search Tree
# 53. Delete In Binary Search Tree
# -----------------------------------------------------------------------------------
# Description:
# Delete the target key K in the given binary search tree if the binary search tree contains K. 
# Return the root of the binary search tree.
# Find your own way to delete the node from the binary search tree, 
# after deletion the binary search tree's property should be maintained.

# -----------------------------------------------------------------------------------
# Assumptions:
# There are no duplicate keys in the binary search tree

# The smallest larger node is first candidate after deletion

#  -----------------------------------------------------------------------------------
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# *************************************************************************************
# Solution:
# !!!! Python has no pointer, so always need to use left / right to link the tree nodes again 
# when updates the tree 
class Solution(object):
  def deleteTree(self, root, key):
    """
    input: TreeNode root, int key
    return: TreeNode
    """
    # if the BST is empty: 
    if not root:
      return root
    #  if root's value > key
    if root.val > key:
      # delete node in the left sub-tree recursivly
      # need root.left since python has no pointer, need to link back nodes after deletion
      root.left = Solution.deleteTree(self, root.left, key)
    #  if root's value < key
    elif root.val < key:
       # delete node in the right sub-tree recursivly
      root.right = Solution.deleteTree(self,root.right, key)
    #  if root's value == key
    else: 
    #  if root has no child or one child: 
      if not root.right:
        return root.left
      if not root.left:
        return root.right
    #  if the root has two children:
      temp = root.right
      #  find the left-most (smallest) node in the right sub-treee:
      while temp.left:
        temp = temp.left
      # Let root's value be that node's value
      root.val = temp.val
      # delet that node's value in the right sub-tree recursively:
      root.right = Solution.deleteTree(self,root.right, temp.val) 
    # return root's value 
    return root