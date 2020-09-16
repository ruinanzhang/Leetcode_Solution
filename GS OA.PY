# 1. Order Check:
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        ordered = heights[:]
        ordered.sort()
        count = 0
        for i in range(len(ordered)):
            if ordered[i] != heights[i]:
                count +=1
        return count
                
# 2. Finding Pairs:
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        count = collections.Counter(nums)
        pair = 0
        seen = []
        for key in count.keys():
            # 没有重复因为总是+，所以找大的
            if k>0 and key+k in count:
                    pair +=1
            # 如果是0，那就找有几个数有重复的就好了
            if k == 0 and count[key]>1:
                    pair +=1
        return pair
# 3.  Meandering Array 
class Solution:
    def MeanderingArray(self, A: List[int]) -> List[int]:
        A.sort()
        left = 0
        right = len(A)-1
        left = 0
        res = []
        while left < right:
            res.append(A[right])
            res.append(A[left])
            left +=1
            right -=1
        return res
#4 condense list:
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return
        cur = head
        values = set()
        values.add(cur.val)
        while cur.next:
            if cur.next.val not in values:
                values.add(cur.next.val)
                cur = cur.next
            else:
                cur.next = cur.next.next
            
        return head
                