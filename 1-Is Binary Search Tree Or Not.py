# 54. Is Binary Search Tree Or Not

# Determine if a given binary tree is binary search tree.
# There should no be duplicate keys in binary search tree.

# Assumptions:

# You can assume the keys stored in the binary search tree can not be Integer.MIN_VALUE or Integer.MAX_VALUE.

# Corner Cases:

# What if the binary tree is null? Return true in this case.
# ------------------------------------------------------------------------------------------------
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#  First thought: Use recursion
#  Base case is if the tree only has one node, then it is a binary tree 
#  Recursive step: if we know for the n-1 level's th nodes if  ->left < the node and its right > the node
#  Then we know at n level the tree is binary tree 
class Solution(object):
 
 
  def isBST(self, root):
    """
    input: TreeNode root
    return: boolean
    """
    # write your solution here

    # Definr integer.min_val and integer.max_val
    INT_MAX = 4294967296
    INT_MIN = -4294967296
    
    return(isBSTUntill(root,INT_MIN,INT_MAX))

 # Need a helper function to record the local min and max of the subtree: 
def isBSTUntill( node,curr_min,curr_max):
  if node == None: 
    return True
  if node.val < curr_min or node.val > curr_max : 
    return False
  else : 
    return isBSTUntill(node.left,curr_min,node.val - 1) and isBSTUntill(node.right,node.val +1,curr_max)


# ***************************************************************************************************
# Summary: similar to "check sorted array" type questions that need left, right ptrs and min/ max 
# Recusive step:
# Base Case: only one node or node == null -> isBST 
# If we know untill the left subtree and right subtree is BST,and this node is < max and > min, we know 
# the whole tree is BST
