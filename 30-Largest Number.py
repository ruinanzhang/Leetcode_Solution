# Tag: Sort Array
#  179. Largest Number
# -----------------------------------------------------------------------------------
# Description:
# Given a list of non negative integers, 
# arrange them such that they form the largest number.
# -----------------------------------------------------------------------------------
# Example 1:
# Input: [3,30,34,5,9]
# Output: "9534330"
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# 思路：merge sort + 特殊的compare function
# 1. 👌👌👌 compare function: 
# 如果str(num1) + stt(num2) > stt(num2) + str(num1)
# 那么组合出来的数字int[str(num1)+str(num2)]就会更大，所以num1在num2前面
# 2. merge sort：
# 就还是老思路，这次重新捋一下：
# 分为两个part：a.separate b.merge
# 2.a Separate: 
# 这里我们就是把一个arr二分，直到分成只有一个数-> Base case
#  def sep(arr,l,r):
#   //Base case: 直到分成只有一个数, return this num
#     if l == r:
        # return[arr[l]]
#   //Recursive steps: 
#   mid = left+ (right-left)//2
#   l = sep(arr,l,mid)
#   r= sep(arr,mid+1,r)
#   return merge(l,r)
# 2.b  Merge(l,r):
#   def Merge(l,r):
#       res = []
#       i = j = 0
#       while i< l(l) and j <l(r): //两边都还有数，没有iterate完
        # ....append compare's res
#       res.extend(l[i:]or r[]j:) // in case 一边有数一边空了，append所有有数的到res的结尾
#       return res
# 3. output int arr to str: 
#  incase we have [0,0,0]
#  use str(int("".join(map(str, arr)))) 👌👌👌👌
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def mergesort(nums,left,right):
            if left == right:
                return [nums[left]]
            mid = left + ((right - left) //2)
            left = mergesort(nums,left,mid)
            right = mergesort(nums,mid+1,right)
            return merge(left,right)
        def compare(str1,str2):
            return str(str1) + str(str2) > str(str2) + str(str1)
        def merge(left,right):
            res = []
            i = j = 0
            while i<len(left) and j<len(right):
                if compare(left[i],right[j]):
                    res.append(left[i])
                    i+=1
                else:
                    res.append(right[j])
                    j+=1
            res.extend(left[i:] or right[j:])
            return res
        n = len(nums)
        left = 0
        right = n-1
        arr = mergesort(nums,left,right)
        return str(int("".join(map(str, arr))))