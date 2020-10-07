# Tag: BST
# 173. Binary Search Tree Iterator
# -----------------------------------------------------------------------------------
# Description:
# Implement an iterator over a binary search tree (BST). Your iterator will be 
# initialized with the root node of a BST.
# Calling next() will return the next smallest number in the BST.
# -----------------------------------------------------------------------------------
# Example 1:
# Input: root = [2,1,3], p = 1
# Output: 2
# Explanation: 1's in-order successor node is 2. Note that both p and the return value is of TreeNode type.
# -----------------------------------------------------------------------------------
# Note:
# next() and hasNext() should run in average O(1) time and uses O(h) memory, 
# where h is the height of the tree.
# You may assume that next() call will always be valid, that is, there will 
# be at least a next smallest number in the BST when next() is called.
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.stack = []
        self.index = -1
        self.inOrderTraverse(root)
    
    def inOrderTraverse(self,root):
        if not root:
            return 
        self.inOrderTraverse(root.left)
        self.stack.append(root.val)
        self.inOrderTraverse(root.right)
        
        

    def next(self) -> int:
        """
        @return the next smallest number
        """
        self.index +=1
        return self.stack[self.index]
        

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return self.index + 1 < len(self.stack)


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()