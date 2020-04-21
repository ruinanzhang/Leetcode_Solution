# Tag : Binary Search Tree
# 135. Closest Number In Binary Search Tree
# -----------------------------------------------------------------------------------
# Description:
# In a binary search tree, find the node containing the 
# closest number to the given target number.
# -----------------------------------------------------------------------------------
# Assumptions:
# There are no duplicate keys in the binary search tree

# The given root is not null.

#  -----------------------------------------------------------------------------------
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# *************************************************************************************
# Solution:
# !!!!!!!Idea: use a helper node to record the node with smallest difference with the target 
# !!!!!!!then, do regular search untill reach a leaf node 

class Solution(object):
  def closest(self, root, target):
    """
    input: TreeNode root, int target
    return: int
    """
    # init helper node as root 
    node = root
    return find_closest_node(node, root, target)

def find_closest_node(node, root,target):
    #  If reach a leaf node, return the node with smallest difference 
    if root is None:
      return node.val
    # If target is a tree node, return the target val 
    if root.val == target:
      return root.val
    # If find a node with smaller difference with the target than the recorded node, change node.val
    if get_dif(root, target) < get_dif(node, target) :
      node.val = root.val
    # Do regular search: 
    if root.val > target : 
      return find_closest_node(node,root.left,target)
    if root.val < target : 
      return find_closest_node(node,root.right,target)

def get_dif(node,target):
  return abs(node.val - target)
