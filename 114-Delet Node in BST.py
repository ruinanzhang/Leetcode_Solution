# Tag: BST
# 450. Delete Node in a BST
# -----------------------------------------------------------------------------------
# Description:
# Given a root node reference of a BST and a key, delete the node with the given key in the BST. 
# Return the root node reference (possibly updated) of the BST.
# Basically, the deletion can be divided into two stages:

# Search for a node to remove.
# If the node is found, delete the node.

# Follow up: Can you solve it with time complexity O(height of tree)?
# -----------------------------------------------------------------------------------
# Example 1:
# Input: root = [5,3,6,2,4,null,7], key = 3
# Output: [5,4,6,2,null,null,7]
# Explanation: Given key to delete is 3. So we find the node with value 3 and delete it.
# One valid answer is [5,4,6,2,null,null,7], shown in the above BST.
# Please notice that another valid answer is [5,2,6,null,4,null,7] and it's also accepted.
# -----------------------------------------------------------------------------------
# Constraints:
# The number of nodes in the tree is in the range [0, 104].
# -105 <= Node.val <= 105
# Each node has a unique value.
# root is a valid binary search tree.
# -105 <= key <= 105
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# 思路: Recursion
# 三种情况：（1）node to be deleted is leaf: node -> Null
# (2) node has right child: node.val = left-most child in right subtree -> delet new node.val from right subtree
# (3) node has no right child but has left child: 
# node.val -> right-most child in left subtree -> delet new node.val from left subtree
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def successor(self, root):
        """
        Find left-most child in right-sub-tree
        """
        root = root.right
        while root.left:
            root = root.left
        return root.val
    
    def predecessor(self, root):
        """
        Find right-most child in left-sub-tree
        """
        root = root.left
        while root.right:
            root = root.right
        return root.val
        
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return None
        
        # delete from the right subtree
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        # delete from the left subtree
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        # delete the current node
        else:
            # the node is a leaf
            if not (root.left or root.right):
                root = None
            # the node is not a leaf and has a right child
            elif root.right:
                root.val = self.successor(root)
                root.right = self.deleteNode(root.right, root.val)
            # the node is not a leaf, has no right child, and has a left child    
            else:
                root.val = self.predecessor(root)
                root.left = self.deleteNode(root.left, root.val)
                        
        return root