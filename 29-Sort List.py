# Tag: Sort
# 148. Sort List
# -----------------------------------------------------------------------------------
# Description:
# Sort a linked list in O(n log n) time using constant space complexity.

# -----------------------------------------------------------------------------------
# Example 1:
# Input: 4->2->1->3
# Output: 1->2->3->4
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# 思路：和merge sort array是一个思路，但要注意find middle and merge都是linked list特有的
# 1. 要merge sort，首先把linked list分成两部分，但是因为没有index，所以分linked list的方式比较特殊：
# fast,slow = head.next,head
# while fast and fast.next:
    # fast = fast.next.next
    # slow = slow.next
# 所以这样下来，slow就是中间的break point
# second = slow.next
# slow.next = None
# l= sort(head)
# r = sort(second)
# return merge(l,r)
# 2.然后 merge也和之前不一样
# 首先因为merge的时候可能会改变head so we need a dummy head 
# def merge(l,r):
#   dummy = ListNode(0)
#   node = dummy 
#   while l and r: （当l 和 r 都没有空的时候）
#       if l.val < r.val: (顺序正确)
#           node.next = l
#           l = l.next
#       elif l.val >=r.val: （顺序不正确）
#           node.next = r
#           r = r.next
#       这个时候node位置之前的已经sor好了，所以不用再看了
#       node = node.next
#   （当l或者r有一个已经看完了）：
#   node.next = l or r
#   return dummy.next
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        # def merge(left,right):
        #     #merge俩list
        # def sort(head):
        #     #sort list
        def merge(head1,head2):
            dummy = ListNode(None)
            node = dummy
            while head1 and head2:
                if head1.val < head2.val:
                    node.next = head1
                    head1 = head1.next
                else:
                    node.next = head2
                    head2 = head2.next
                node = node.next
            node.next = head1 or head2
            return dummy.next
#             if not left:
#                 return right
#             if not right:
#                 return left
#             if left.val > right.val:
#                 left,right = right,left
#             new_head = left
#             while left and right:
#                 if left.val < right.val:
#                     left = left.next
#                 else:
#                     new = right.next
#                     right.next = new.next
#                     left.next = right
#                     new.next = left
#                     left = new 
# #             肯定有一边已经没有了
#             new_head.next = left or right
#             return new_head
        def sort(head):
            if not head or not head.next:
                return head
            # divide list into two parts
            fast, slow = head.next, head
            while fast and fast.next:
                fast = fast.next.next
                slow = slow.next
            second = slow.next
            # cut down the first part
            slow.next = None
            l = sort(head)
            r = sort(second)
            return merge(l, r)
        #     mid = n//2
        #     if not head or not head.next:
        #         return head
        #     breakpoint = head
        #     i = 0
        #     while i < mid-1:
        #         breakpoint = breakpoint.next
        #         i+=1
        #     second = breakpoint.next
        #     breakpoint.next = None 
        #     left = sort(head,mid)
        #     right = sort(second,n-mid+1)
        #     return merge(left,right)
        if not head or not head.next:
            return head
        
        dummy = ListNode(0)
        dummy.next = head 
        n = 1 
        count = head
#       Find the length of linkedList
        while count.next:
            n+=1
            count = count.next
        res = sort(head)
        return res
        
