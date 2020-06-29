# Tag: Sort Array
# 56. Merge Intervals
# -----------------------------------------------------------------------------------
# Description:
# Given a collection of intervals, merge all overlapping intervals.
# -----------------------------------------------------------------------------------
# Example 1:
# Input: [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# 思路：
#   1. merge sort arr in interval lists by the start numer O(nlogn)
#   2.merge intervals in order O(n)
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        
        def sort(intervals,left,right):
            if left == right:
                k = intervals[left]
                return [k]
            mid = left + (right-left)//2
            left = sort(intervals,left,mid)
            right = sort(intervals,mid+1,right)
            return mergearr(left,right)
        def mergearr(left,right):
            i = j =0
            res = []
            while i < len(left) and j < len(right):
                if left[i][0] < right[j][0]:
                    res.append(left[i])
                    i+=1
                else: 
                    res.append(right[j])
                    j+=1
            res.extend(left[i:] or right[j:])
            return res
        def mergeinterval(arr1,arr2):
            if arr1[1]<=arr2[1]:
                return [arr1[0],arr2[1]]
            else:
                return [arr1[0],arr1[1]]
            
        n = len(intervals)
        if n == 0:
            return intervals
    
        left = 0
        right = n-1
        sorted_int = sort(intervals,left,right)
        # sorted_int = intervals
        i = 0
        res = []
        while i+1 < len(sorted_int):
            if sorted_int[i+1][0] <= sorted_int[i][1]:
                res =  mergeinterval(sorted_int[i],sorted_int[i+1])
                sorted_int.pop(i)
                sorted_int[i] = res
            else:
                i+=1
            
            
        return sorted_int

            