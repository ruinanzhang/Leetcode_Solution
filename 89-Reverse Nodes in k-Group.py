# Tag: Recursion + LinkedList
# 25. Reverse Nodes in k-Group
# -----------------------------------------------------------------------------------
# Description: 

# k is a positive integer and is less than or equal to the length of the linked list. 
# If the number of nodes is not a multiple of k then left-out nodes in the end should
#  remain as it is.
# -----------------------------------------------------------------------------------
# Note:

# Only constant extra memory is allowed.
# You may not alter the values in the list's nodes, only nodes itself may be changed.
# -----------------------------------------------------------------------------------
# Example:

# Given this linked list: 1->2->3->4->5

# For k = 2, you should return: 2->1->4->3->5

# For k = 3, you should return: 3->2->1->4->5
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# 思路：
# 很明显是recursion，但recursion的条件有点复杂
# 首先需要一个reverse function (from 86-Reverse linked-list)
# Base Case: not head: return 
# Recursive Step:
# 每次 head = head.next for k elements 
# 暂时保存head的value: curr
# reverse从head开始k个element：
# reversed_head = reverse(curr,k) //if not enough k element, do not reverse
# 然后接上之后已经reversed好了的：
# temp = re_head
#             while temp.next:
#                 temp = temp.next
#             temp.next= recursion(head,k)
# return re_head
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        # This is my reverse function, will return the reversed head 
        # will reverse k elements from given head -- if exists 
        def reverse(head,k):
            curr = head 
            prev = None
            i = 0
            while i<k and curr:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
                i +=1
            return prev
        def recursion(head,k):
            # This is my recursion function that will recursivly reverse nodes in K-group 
            # Base case if no more elments, return:
            if not head:
                return 
            # recursive step: always reverse k elements and .next to reversed sub_sol
            # will reverse first k elements:
            i = 0
            curr = head
            while i < k and head:
                head = head.next
                i +=1
            if i == k:
                re_head = reverse(curr,k)
            if i<k:
                re_head = curr
            temp = re_head
            while temp.next:
                temp = temp.next
            temp.next= recursion(head,k)
            return re_head
        return recursion(head,k)