# Tag: Recurssion + DFS
# 107. Binary Tree Level Order Traversal II
# -----------------------------------------------------------------------------------
# Description:
# Given a binary tree, return the bottom-up level order traversal of its nodes' values.
#  (ie, from left to right, level by level from leaf to root).
# -----------------------------------------------------------------------------------
# Example:
# Given binary tree [3,9,20,null,null,15,7],
#     3
#    / \
#   9  20
#     /  \
#    15   7
# Return its bottom-up level order traversal as:
# [
#   [15,7],
#   [9,20],
#   [3]
# ]
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# 思路：
# 👌👌👌 重点：！！！dfs的时候用一个level list 把每个level的node放进去，
# level_list[level].append(node.val)
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        level_list = []
        def dfs(root,lv):
#           如果刚进入新的一层
            if len(level_list) == lv:
#           准备好一个新的【】备用
                level_list.append([])
            level_list[lv].append(root.val)
            if root.left:
                dfs(root.left,lv+1)
            if root.right:
                dfs(root.right,lv+1)
#           如果左右都没有就直接return回上一个recursive step了
        if not root:
            return []
        dfs(root,0)
        return level_list[::-1]
            
             