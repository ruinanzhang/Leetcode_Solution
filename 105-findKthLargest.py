# Tag: Heapq
# 215. Kth Largest Element in an Array
# -----------------------------------------------------------------------------------
# Description: 

# Find the kth largest element in an unsorted array. Note that it is the kth largest 
# element in the sorted order, not the kth distinct element.
# -----------------------------------------------------------------------------------
# Example 1:
# Input: [3,2,1,5,6,4] and k = 2
# Output: 5

# Example 2:
# Input: [3,2,3,1,2,4,5,5,6] and k = 4
# Output: 4
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# 思路：
# construct heap: O(n)
# poo heap: (n-k)O(log(n))
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for num in nums:
            heapq.heappush(heap, num)
        for x in range(0,len(nums)-k):
            heapq.heappop(heap)
        return heapq.heappop(heap)