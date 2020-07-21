# Tag: Linked-List + Math
# 2. Add Two Numbers
# -----------------------------------------------------------------------------------
# Description:
# You are given two non-empty linked lists representing two non-negative integers. 
# The digits are stored in reverse order and each of their nodes contain a single digit.
#  Add the two numbers and return it as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
# -----------------------------------------------------------------------------------
# Example:

# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.
# -----------------------------------------------------------------------------------

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# 思路：基本就是小学两位数相加的算法
# * 有一点值得注意的是：有可能出现 999 + 1 = 1000， 一个比数另一个多几位数这种情况！
# 所以while的条件是l1 or l2 
# and if null, node.val = 0; node does not point to the next node
# 最后如果还需要进位但是not l1 and not l2: head.next = ListNode(1)
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        def add2nodes(node1,node2,plus):
            if not node1:
                v1 = 0
            else: 
                v1 = node1.val
            if not node2:
                v2 = 0
            else:
                v2 = node2.val
            sum_num = v1 + v2 + plus
            if sum_num <=9:
                res = sum_num
                plus = 0
            elif sum_num >=10:
                res = sum_num -10
                plus=1
            return plus,ListNode(res)
        res =""
        plus = 0
        dummy= ListNode(-1)
        head = dummy
        while l1 or l2:
            plus,head.next = add2nodes(l1,l2,plus)
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            head= head.next
        if plus ==1:
            head.next = ListNode(1)    
        return dummy.next
        
    