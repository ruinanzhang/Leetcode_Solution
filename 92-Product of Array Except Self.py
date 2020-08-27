# Tag: Array + 特殊silu ***
# 238. Product of Array Except Self
# -----------------------------------------------------------------------------------
# Description: 

# Given an array nums of n integers where n > 1,  return an array output such that 
# output[i] is equal to the product of all the elements of nums except nums[i].
# -----------------------------------------------------------------------------------
# Constraint:
# It's guaranteed that the product of the elements of any prefix or suffix of the array 
# (including the whole array) fits in a 32 bit integer.

# Note: Please solve it without division and in O(n).
# -----------------------------------------------------------------------------------
# Example:

# Input:  [1,2,3,4]
# Output: [24,12,8,6]
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# 思路：
# 如果可以用divisoon就很简单，先算出总乘机，iterate每个divide每个item
# 不能用division：
# 从左到右iter，算每个数left的product
# 再reverse，从右到左，算每个数right的product
# 再iterate 除去每个数的product=left * right
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # The length of the input array 
        length = len(nums)
        
        # The left and right arrays as described in the algorithm
        L, R, answer = [0]*length, [0]*length, [0]*length
        
        # L[i] contains the product of all the elements to the left
        # Note: for the element at index '0', there are no elements to the left,
        # so the L[0] would be 1
        L[0] = 1
        for i in range(1, length):
            
            # L[i - 1] already contains the product of elements to the left of 'i - 1'
            # Simply multiplying it with nums[i - 1] would give the product of all 
            # elements to the left of index 'i'
            L[i] = nums[i - 1] * L[i - 1]
        
        # R[i] contains the product of all the elements to the right
        # Note: for the element at index 'length - 1', there are no elements to the right,
        # so the R[length - 1] would be 1
        R[length - 1] = 1
        for i in reversed(range(length - 1)):
            
            # R[i + 1] already contains the product of elements to the right of 'i + 1'
            # Simply multiplying it with nums[i + 1] would give the product of all 
            # elements to the right of index 'i'
            R[i] = nums[i + 1] * R[i + 1]
        
        # Constructing the answer array
        for i in range(length):
            # For the first element, R[i] would be product except self
            # For the last element of the array, product except self would be L[i]
            # Else, multiple product of all elements to the left and to the right
            answer[i] = L[i] * R[i]
        
        return answer