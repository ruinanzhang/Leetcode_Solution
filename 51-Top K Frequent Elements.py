# Tag: Hash Table, Heap
# 347. Top K Frequent Elements
# -----------------------------------------------------------------------------------
# Description:
# Given a non-empty array of integers, return the k most frequent elements.
# -----------------------------------------------------------------------------------
# Example 1:
# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
# -----------------------------------------------------------------------------------
# Notes:
# You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
# Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
# It's guaranteed that the answer is unique, in other words the set of the top k frequent elements is unique.
# You can return the answer in any order.
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# 思路：
# 1. hashmap map {item:frequency} 
# 2. sort hashmap by frequency
# 重点：*** 如何sort一个dic：
# ***sorted(dict, key = dict.get,reverse = True/False)***
# 这么做的time is: nlogn
# if use heap, then time comlexity is nlogk
# 用heap的写法： heapq.nlargest(k, count.keys(), key=count.get) 
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        fmap = {}
        for ind, num in enumerate(nums):
            fmap[num] = fmap.get(num,0) + 1
        arr = sorted(fmap, key = fmap.get,reverse = True)
        return arr[:k]