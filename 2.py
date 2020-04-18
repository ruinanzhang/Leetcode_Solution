# Tag : Binary Search Tree

# 51. Insert In Binary Search Tree
# -----------------------------------------------------------------------------------
# Description:

# Insert a key in a binary search tree if the binary search tree does not already contain the key.
#  Return the root of the binary search tree.

# -----------------------------------------------------------------------------------
# Assumptions:

# There are no duplicate keys in the binary search tree
# If the key is already existed in the binary search tree, you do not need to do anything
# -----------------------------------------------------------------------------------

# 
# # Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# ***********************************************************************************

# Solution: 
class Solution(object):
  def insert(self, root, key):
    """
    input: TreeNode root, int key
    return: TreeNode
    """
    # Base case: 
    # If root is None, insert the key to the root: 
    if root is None: 
      node = TreeNode(key)
      root = node 
    #  If root is not None, We check root's value
    else:
        # If root's val < key: we check if root-> left, if it's None, we insert the new key 
        # If root->left is not None, we recursivly do the previsou steps untill we find 
        # A paprent of a leaf node
        if root.val < key: 
            if root.right is None: 
                node = TreeNode(key)
                root.right = node 
            else: 
                Solution.insert(self,root.right,key) 
        # Same for if root's val > key
        if root.val > key: 
            if root.left is None: 
                node = TreeNode(key)
                root.left = node 
            else: 
                Solution.insert(self, root.left, key) 
        # if root.val == key: 
          # Do nothing
    
    return root
