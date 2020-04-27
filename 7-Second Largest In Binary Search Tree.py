# Tag : Binary Search Tree
#347. Second Largest In Binary Search Tree
# -----------------------------------------------------------------------------------
# Description:
# Find the second largest key in the given binary search tree.
# If there does not exist the second largest key, return Integer.MIN_VALUE.
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
# !!! Look for better solution 
class Solution(object):
  def secondLargest(self, root):
    """
    input: TreeNode root
    return: int
    """
    
    if root.right is None:
      if root.left is None:
        return -2147483648
      res = get_most_right(root.left)
      return res.val
    return find_second_largest(root,root.right)
    # write your solution here
def find_second_largest(prev,node):
  if node.right is None:
    if node.left is None:
      return prev.val
    else: 
      res = get_most_right(node.left)
      return res.val
      
  else:
    return find_second_largest(node,node.right)
def get_most_right(node):
  while node.right:
    node = node.right
  return node


# !!!!!! Better solution: 
 def largestSmaller(self, root, target):
    """
    input: TreeNode root, int target
    return: int
    """
    # First let temp = int_min which is -2147483648
    temp = -2147483648
    # while root is not None:
    while root:
      # if root.val >=target,go to the left sub tree
      if root.val >= target:
        root = root.left
      # if root.val < target, go to right sub tree untill find the largest smaller than target
      else :
        temp = root.val
        root = root.right
    return temp