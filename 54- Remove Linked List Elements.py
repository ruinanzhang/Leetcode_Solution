# Tag: Linked-List + Recurrsion
# 203. Remove Linked List Elements
# -----------------------------------------------------------------------------------
# Description:
# Remove all elements from a linked list of integers that have value val.
# -----------------------------------------------------------------------------------
# Example:
# Input:  1->2->6->3->4->5->6, val = 6
# Output: 1->2->3->4->5
# -----------------------------------------------------------------------------------

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# 思路：
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
# 1.Iter solution:

        dummy = ListNode(-1)
        dummy.next = head
        node = dummy
        while head:
            if head.val == val:
                node.next = head.next
                head = head.next
            else:
                head = head.next
                node = node.next
        return dummy.next
# 2. Recurssive solution:
        def rec(node,val):
            if node:
                if node.val == val:
                    return rec(node.next,val)
                else:
                    node.next = rec(node.next,val)
                return node
        return rec(head,val)