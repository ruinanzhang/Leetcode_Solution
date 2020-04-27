# Tag : Binary Search Tree
# 452. Kth Smallest Element in a BST
# -----------------------------------------------------------------------------------
# Description:
# Given a binary search tree, write a function 
# kthSmallest to find the kth smallest element in it.
# -----------------------------------------------------------------------------------
# Assumptions:
# You may assume k is always valid, 1 <=k <= BST's total elements.
# -----------------------------------------------------------------------------------
# Follow-up:
# What if the BST is modified (insert/delete operations) often and you need to find the
#  kth smallest frequently? How would you optimize the kthSmallest routine?
#  -----------------------------------------------------------------------------------
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# *************************************************************************************
# Solution 1 : in-order traverse + list (Time : O(N))
# It's easy to comr up with a O(N):
class Solution(object):
  def kthSmallest(self, root, k):
    """
    input: TreeNode root, int k
    return: int
    """
    res = []
    res = inorder(root,res)
    return res[k-1]

    
   
def inorder(root,res):
    if root.left:
      inorder(root.left,res)
    res.append(root.val)
    if root.right:
      inorder(root.right,res)
    return res

# Solution 2: for unbalanced tree (all nodes in left sub) :O(N+h)????
#  binary search (recursive)
class Solution(object):
  def kthSmallest(self, root, k):
    """
    input: TreeNode root, int k
    return: int
    """
    count_num = count(root.left)
    if k <= count_num :
      return Solution.kthSmallest(self,root.left, k )
    if k > count_num + 1 :
      return Solution.kthSmallest(self,root.right, k-1-count_num)
    return root.val

def count(root):
  if not root:
    return 0
  return 1 + count(root.left) + count(root.right)