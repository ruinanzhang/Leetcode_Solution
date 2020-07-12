# Tag: Doubly Linked List
# 430. Flatten a Multilevel Doubly Linked List
# -----------------------------------------------------------------------------------
# Description:
# You are given a doubly linked list which in addition to the next and previous pointers, 
# it could have a child pointer, which may or may not point to a separate doubly linked list. 
# These child lists may have one or more children of their own, and so on, to produce a multilevel
#  data structure, 
# as shown in the example below.

# Flatten the list so that all the nodes appear in a single-level, 
# doubly linked list. You are given the head of the first level of the list.
# -----------------------------------------------------------------------------------
# Example:
# Input: head = [1,2,3,4,5,6,null,null,null,7,8,9,10,null,null,11,12]
# Output: [1,2,3,7,8,11,12,9,10,4,5,6]
# We use the multilevel linked list from Example 1 above:
#  1---2---3---4---5---6--NULL
#          |
#          7---8---9---10--NULL
#              |
#              11--12--NULL
# [1,2,3,4,5,6,null]
# [7,8,9,10,null]
# [11,12,null]
# -----------------------------------------------------------------------------------
# Note: 
# Number of Nodes will not exceed 1000.
# 1 <= Node.val <= 10^5
# -----------------------------------------------------------------------------------
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# 思路：5 situations:
# 1. not head -> return
# 2. not head.child && not head.next -> (最后一个node) if stack-> head.next = stack.pop()
#  if not stack: return 
# 3. not head.child && head.next -> head = head.next (直接看下一个)
# 4. head.child and not head.next: head.next = head.child
# 5. head.child and head.next: 
# stack.append(head.next) 
# head.next = head.child,
# head.child = None 
# head.next.prev = head !!!!因为是doubly所以要handle一下head.prev
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""
class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        dummy = Node(0)
        dummy.next = head 
        stack =[]
#       CASE 1: 
        if not head:
            return 
        while head:
    #       IF CHILD:
            if head.child:
    #         CASE 5 If NEXT: 
                if head.next:
                    stack.append(head.next)
    #         CASE 4 IF NEXT:
                head.next = head.child
                head.next.prev = head 
                head.child = None
    #       CASE 2
            elif not head.next and stack:
                head.next = stack.pop()
                head.next.prev = head
        # CASE 3
            head = head.next 
        
        return dummy.next
#          


                
                
                
        