# Tag: Recurssion + Linked List
# 24. Swap Nodes in Pairs
# -----------------------------------------------------------------------------------
# Description:
# Given a linked list, swap every two adjacent nodes and return its head.
# You may not modify the values in the list's nodes, only nodes itself may be changed.
# -----------------------------------------------------------------------------------
# Example 1:
# Given 1->2->3->4, you should return the list as 2->1->4->3.
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# 思路：
# 1. 从头开始，做recursion
# 2. Base case: 如果not head or not head.next (俩俩看还剩一个数 或者没有数了--->> return head)
# 3. Recussive step: 如果每次往后看都还有数，position.next.next = swap(position.next.next)
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        
        def swap(head):
            dummy = ListNode(0)
            dummy.next = head 
            if not head or not head.next:
                return head
            curr = head
            p = dummy
            new = head.next
            curr.next =  new.next
            new.next = p.next
            p.next = new 
            p.next.next.next = self.swapPairs(p.next.next.next)
            return dummy.next
        if not head:
            return 
        return swap(head)

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# Better solution!!! 
class Solution(object):
    def swapPairs(self, head: ListNode) -> ListNode:
        """
        :type head: ListNode
        :rtype: ListNode
        """

        # If the list has no node or has only one node left.
        if not head or not head.next:
            return head

        # Nodes to be swapped
        first_node = head
        second_node = head.next

        # Swapping
        first_node.next  = self.swapPairs(second_node.next)
        second_node.next = first_node

        # Now the head is the second node
        return second_node
        