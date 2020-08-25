# Tag: Two Pointers + LinkedList
# 19. Remove Nth Node From End of List
# -----------------------------------------------------------------------------------
# Description: 

# Given a linked list, remove the n-th node from the end of list and return its head.
# -----------------------------------------------------------------------------------
# Note:

# Given n will always be valid.
# -----------------------------------------------------------------------------------
# Example:
# Given linked list: 1->2->3->4->5, and n = 2.

# After removing the second node from the end, the linked list becomes 1->2->3->5.
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# 思路：
# 1. Use 2 ptrs, 1st and 2nd, keep them n pos from each other
# 2. When 2nd reaches end, 1st is the number that need to be deleted
# 3. if the 1st number is to be deleted, return head.next()

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head 
        
        first = second = head
        for i in range(n):
            second = second.next
        if not second:
            return head.next
        while second.next:
            second = second.next
            first = first.next
        new = first.next.next
        first.next = new
        return dummy.next