# Tag: LinkedList
# 160. Intersection of Two Linked Lists
# -----------------------------------------------------------------------------------
# Description:
# Write a program to find the node at which the intersection of two singly linked lists begins.
# -----------------------------------------------------------------------------------
# Example 1:
# Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3
# Output: Reference of the node with value = 8
# Input Explanation: The intersected node's value is 8 (note that this must not be 0 if the two lists intersect). 
# From the head of A, it reads as [4,1,8,4,5]. From the head of B, it reads as [5,6,1,8,4,5]. 
# There are 2 nodes before the intersected node in A; There are 3 nodes before the intersected node in B.
# -----------------------------------------------------------------------------------
# Note:
# If the two linked lists have no intersection at all, return null.
# The linked lists must retain their original structure after the function returns.
# You may assume there are no cycles anywhere in the entire linked structure.
# Each value on each linked list is in the range [1, 10^9].
# Your code should preferably run in O(n) time and use only O(1) memory.
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# 思路: iterate thru two lists, get length and diff, set start at the same length, check each point
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        # changeA = True
        if not headA and not headB:
            return None
        lenA = 0
        lenB = 0
        dummyA = ListNode(0)
        dummyA.next = headA
        dummyB = ListNode(0)
        dummyB.next = headB
        while headA:
            lenA +=1
            headA = headA.next
        while headB:
            lenB +=1
            headB = headB.next
        headA = dummyA.next
        headB = dummyB.next
        if lenA > lenB:
            diff = lenA-lenB
            while diff>0:
                headA = headA.next
                diff -=1
        if lenB > lenA:
            diff = lenB-lenA
            while diff>0:
                headB = headB.next
                diff -=1
        while headA != headB:
            headA = headA.next
            headB = headB.next
        return headA
        