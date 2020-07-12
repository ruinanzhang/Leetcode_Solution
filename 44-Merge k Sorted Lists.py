# Tag: Min heap + linked list
# 23. Merge k Sorted Lists
# -----------------------------------------------------------------------------------
# Description:
# Merge k sorted linked lists and return it as one sorted list.
# Analyze and describe its complexity.
# -----------------------------------------------------------------------------------
# Example:
# Input:
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# Output: 1->1->2->3->4->4->5->6
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# 思路：
#       用priority queue:
#       举个栗子：
#       input: 
#       List 1: 1->4->5,
#       List 2: 1->3->4,
#       List 3: 2->6
#       pq = priority_queue()
#       (1)每个list我们最开始都从head开始，先把所有heads put into a pq
#       (2)Then we pop from the front of the pq, pop() into ans
#       (3)From the poped list, move the head pointer from head to the next
#       (4)Push head.next to the pq
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
import heapq
class Solution(object):
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
#       if input is null
        if not lists:
            return 
#       Since we might change head-> use a dummy head
        dummy = ListNode(0)
        newhead = dummy
#       Init our pq
        pq = []
#       !!! We need index cuz we need to track the list number (which list where are poping from later)
        for ind, l in enumerate(lists):
            if l:
                heapq.heappush(pq,(l.val,ind))
#       当pq里面还有数当时候：
        while pq:
            # 从pq pop最小的数：
            val, list_number = heapq.heappop(pq)
            # 接在ans list的后面
            curr = ListNode(val)
            newhead.next = curr
            newhead = newhead.next
            node = lists[list_number] 
            # 如果此list后面还有数：
            if node.next:
                heapq.heappush(pq,(node.next.val,list_number))
                lists[list_number] = node.next
            node = node.next
        return dummy.next