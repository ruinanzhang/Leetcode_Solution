# Tag: Sort Array
# 315. Count of Smaller Numbers After Self
# -----------------------------------------------------------------------------------
# Description:
# You are given an integer array nums and you have to return a new counts array.
# The counts array has the property where counts[i] is the number of smaller 
# elements to the right of nums[i].
# -----------------------------------------------------------------------------------
# Example 1:
# Input: [5,2,6,1]
# Output: [2,1,1,0] 
# Explanation:
# To the right of 5 there are 2 smaller elements (2 and 1).
# To the right of 2 there is only 1 smaller element (1).
# To the right of 6 there is 1 smaller element (1).
# To the right of 1 there is 0 smaller element.
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# 思路：
#   还是merge sort的思路，但是merge sort的同时，把larger number放到前面
#   并且track有几个数被放到了当前这个数的前面在merge的时候
#   有几个比这个数小的数 = 有多少个数从right被移动到了left
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
#   思路：还是merge sort的思路，但是merge sort的同时，track有几个数被放到了当前这个数的前面在merge的时候
       
    
        def divide(pairs):
            if len(pairs) == 1:
                return pairs
            mid = len(pairs) // 2
            left = divide(pairs[:mid])
            right = divide(pairs[mid:])
            return conquer(left, right)
        
        def conquer(l,r):
            i = j = 0
            sort = []
            while (i< len(l)) and  (j< len(r)):
                if l[i][0] > r[j][0]:
                    sort.append(l[i])
                    res[l[i][1]] += len(r)-j
                    i +=1
                else: 
                    sort.append(r[j])
                    j +=1
            sort.extend(l[i:] or r[j:])
            return sort
        n = len(nums)
        if not n:
            return []
        res = [0] * len(nums)
        pairs = [(n,i) for i,n in enumerate(nums)]
        divide(pairs)
        return res