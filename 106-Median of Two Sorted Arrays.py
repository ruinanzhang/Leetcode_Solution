# Tag: Array, 2 ptrs
# 4. Median of Two Sorted Arrays
# -----------------------------------------------------------------------------------
# Description: 

# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the 
# median of the two sorted arrays.
# Follow up: The overall run time complexity should be O(log (m+n)).
# -----------------------------------------------------------------------------------
# Example 1:
# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.

# Example 2:
# Input: nums1 = [1,2], nums2 = [3,4]
# Output: 2.50000
# Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# 思路：
# use 2 ptrs, find half of the total size -> median of the two sorted arrays 
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1, n2 = len(nums1), len(nums2)
        n = n1 + n2
       
        end = n // 2    
        i, i1, i2  = 0, 0, 0             # Pointer for implict merge list, nums1 pointer, nums2 pointer 
        current, previous = 0, 0         # current and previous value in implict merge
        
        # Implictly build half of the sorted merge list
        # but only save last values
        while i <= end:
            previous = current
            if i1 == n1:                 # First list is exhausted ==> choose from second list
                current = nums2[i2] 
                i2 += 1
            elif i2 == n2:               # Second list ist exhaused ==> choose from first list
                current = nums1[i1]
                i1 += 1
            elif nums1[i1] < nums2[i2]:  # Choose element from first list
                current = nums1[i1]
                i1 += 1
            else:                        # Choose element from second list
                current = nums2[i2]      
                i2 += 1

            i += 1
        
        if n % 2 == 0:
            return (previous + current) / 2.0
        else: 
            return current