# Tag : Binary Search Tree
# 55. Get Keys In Binary Search Tree In Given Range
# -----------------------------------------------------------------------------------
# Description:
# Get the list of keys in a given binary search tree in a 
# given range[min, max] in ascending order, both min and max are inclusive.
# -----------------------------------------------------------------------------------
# Corner Case: 
# What if there are no keys in the given range? Return an empty list in this case.
# -----------------------------------------------------------------------------------
# Assumptions:
# The given binary search tree is not null.

#  -----------------------------------------------------------------------------------
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# *************************************************************************************
# !!!! traverse the tree from small to large, put the node's value to the list if its wihtin the range
class Solution(object):
  def getRange(self, root, min, max):
    """
    input: TreeNode root, int min, int max
    return: Integer[]
    """
    list = []
    traverse(root,list,min,max)
    return list
    # write your solution here
def traverse(root,list,min,max):
  if root:
    if root.left:
      traverse(root.left,list,min,max)
    if root.val >= min and root.val <= max :
      list.append(root.val)
    if root.right:
      traverse(root.right,list,min,max)