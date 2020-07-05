# Tag: Sort
# 147. Insertion Sort List
# -----------------------------------------------------------------------------------
# Description:

# A graphical example of insertion sort.
#  The partial sorted list (black) initially contains only the first element in the list.
# With each iteration one element (red) is removed from the input data and
# inserted in-place into the sorted list.

# Algorithm of Insertion Sort:

# Insertion sort iterates, consuming one input element each repetition, and growing a sorted output list.
# At each iteration, insertion sort removes one element from the input data, finds the location it belongs within the sorted list, and inserts it there.
# It repeats until no input elements remain.
# -----------------------------------------------------------------------------------
# Example:
# Input: 4->2->1->3
# Output: 1->2->3->4
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# 思路：三个ptr！current node: curr, insert position: p_in, dummy head node: dummy
# (The reason to have dummy as head is because we might change head node)
# 整体思路就是，找到一个node比之前的node的值要小,把它insert到应该去的pos，
# 然后继续，这样每次做完insert position 之前的所有node都是sort好了的
#

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        p_in = dummy = ListNode(0)
        curr = dummy.next = head

        while curr and curr.next:

            if curr.val < curr.next.val:
                curr = curr.next
                continue
            else:
                if p_in.next.val > curr.next.val:
                    p_in = dummy
                while p_in.next.val < curr.next.val:
                    p_in = p_in.next
                # ----以下是错误思路！！Linked list切忌swap value，but change node.next and such
                # temp = p_in.next.val
                # p_in.next.val = curr.next.val
                # curr.next.val = temp
                # p_in.next = curr.next

                # 解释以下这里，如果我们的list长这样：0->4->2->1->3
                # curr : 4->2->1->3
                # curr.next : 2->1->3
                # new = 2->1->3
                # 然后我们让curr.next = new.next　 这样就相当于remove了curr.next which is [2]
                # curr.next = 1->3
                # curr = 4->1->3
                # 这时候我们的p_in.next : 4->1->3
                # new.next = p_in.next
                # 这就相当于insert了4->1->3到2之后
                # new：2->4->1->3
                # 这个时候让 p_in.next = new
                # dummy 就变成了 0->2->4->1->3
                new = curr.next
                curr.next = new.next
                new.next = p_in.next
                p_in.next = new

        return dummy.next
