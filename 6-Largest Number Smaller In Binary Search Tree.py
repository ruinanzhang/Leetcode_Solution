# Tag : Binary Search Tree
# 135. Closest Number In Binary Search Tree
# -----------------------------------------------------------------------------------
# Description:
# In a binary search tree, find the node containing 
# the largest number smaller than the given target number.
# If there is no such number, return -2^31.
# -----------------------------------------------------------------------------------
# Assumptions:
# The given root is not null.
# There are no duplicate keys in the binary search tree.

#  -----------------------------------------------------------------------------------
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# *************************************************************************************
# Solution:
# !!!! Similar to find the cloest
# !!!! The condition to update helper node is different 
# !!!! Might have better solution, this is hacky 
  def largestSmaller(self, root, target):
    """
    input: TreeNode root, int target
    return: int
    """
    r_val = root.val
    node = root
    #  If root is the node we re looking for:
    if root.val < target and root.right is None:
      return root.val
    res = find_node(node, root,target)
    # if we can't find such node, we will return the root node value and if it's larger than the target,
    # we can't find target 
    # else it might be our target is the root 
    if res >= target:
      return -2147483648
    else: 
      return res

def find_node(node, root,target):
    #  If reach a leaf node, return the node with smallest difference 
    if root is None:
      return node.val
   
    # If helper node's value is ever be the target, update it 
    if get_dif(node,target) == 0:
      node.val = root.val
    # If curr node smaller than target:
    if root.val < target:
    # If value in hepler node larger than target, update anyway 
      if node.val >= target:
        node.val = root.val
      else:
        # If value in hepler node is already smaller, update when have smaller difference 
        if get_dif(root, target) < get_dif(node, target):
          node.val = root.val
    # Do regular search: 
    if root.val >= target : 
      return find_node(node,root.left,target)
    if root.val < target : 
      return find_node(node,root.right,target)

def get_dif(node,target):
  return abs(node.val - target)