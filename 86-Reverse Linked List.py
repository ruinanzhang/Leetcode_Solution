# Tag: LinkedList + Recursion
# 206. Reverse Linked List
# -----------------------------------------------------------------------------------
# Description: 

# Reverse a singly linked list.
# -----------------------------------------------------------------------------------
# Example:

# Input: 1->2->3->4->5->NULL
# Output: 5->4->3->2->1->NULL
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# 思路：
# 两种做法：recurrsion and iterative 
# 😺骚气 recurssion: 
# Base case: if not head or not head.next: return head
# Recursive_step: curr_head = Recurfuction(head.next)
# head.next.next = head (往回指)
# head.next = null (断cycle)
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# 😺骚气 recurssion
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head 
        curr = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return curr
# 😺iterative
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        curr = head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
       
        return prev