# Tag: BST + Recursion
# 889. Construct Binary Tree from Preorder and Postorder Traversal
# -----------------------------------------------------------------------------------
# Description:
# Return any binary tree that matches the given preorder and postorder traversals.
# Values in the traversals pre and post are distinct positive integers.
# -----------------------------------------------------------------------------------
# Example:
# Input: 
# Input: pre = [1,2,4,5,3,6,7], post = [4,5,2,6,7,3,1]
# Output: [1,2,3,4,5,6,7]
# -----------------------------------------------------------------------------------
# Note: 
# 1 <= pre.length == post.length <= 30
# pre[] and post[] are both permutations of 1, 2, ..., pre.length.
# It is guaranteed an answer exists. If there exists multiple answers, you can return any of them
# -----------------------------------------------------------------------------------
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# 思路，注意pre和post分别是怎么走的！！！
# if input: [1,2,3,5,6,9,10]
# pre: root-> root.left->root.right = [1,2,5,9,10,6,3]
# post:root.left->root.right->root = [9,10,5,6,2,3,1]
# 第一注意到的：pre[0] == post[-1] = [1] is root
# 用divde conquer来思考，
# 相应的，pre[1] which is 2 is the subleft tree root while post[-2] = 3 is the subright tree root
# if pre[1] == post[-2]说明没有right tree or right tree, 为了方便期间就假设没有right tree
# 所以sub prob的形式： [root,(left nodes),(rigt nodes)]
# 所以[1,2,5,9,10,6,3] -> [1,(2,5,9,10,6),(3)] 
# [2,5,9,10,6] ->[2,(5,9,10),(6)]
# 最后我们需要construct一个root node,
# root.left = recursively 重复上面的！sub left = pre[1:leftNodeCount+1] sub right: [:leftNodeCount]
# root.right =  recursively 重复上面的！pre[leftNodeCount+1:],post[leftNodeCount:-1]
# return root就好了
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, pre: List[int], post: List[int]) -> TreeNode:
        if not pre:
            return 
        root = TreeNode(pre[0])
        if len(pre)>1:
            leftNodeCount = post.index(pre[1]) + 1
            root.left = self.constructFromPrePost(pre[1:leftNodeCount+1],post[:leftNodeCount])
            root.right =  self.constructFromPrePost(pre[leftNodeCount+1:],post[leftNodeCount:-1])
        return root
            
        
        