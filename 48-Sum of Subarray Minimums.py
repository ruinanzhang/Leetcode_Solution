# Tag: Monotonic Stack ❗️❗️❗️❗️❗️❗️❗️❗️❗️❗️❗️❗️❗️
# 907. Sum of Subarray Minimums
# -----------------------------------------------------------------------------------
# Description:
# Given an array of integers A, find the sum of min(B), where B ranges over every 
# (contiguous) subarray of A.
# Since the answer may be large, return the answer modulo 10^9 + 7.
# -----------------------------------------------------------------------------------
# Example:
# Input: [3,1,2,4]
# Output: 17
# Explanation: Subarrays are [3], [1], [2], [4], [3,1], [1,2], [2,4], [3,1,2], [1,2,4], [3,1,2,4]. 
# Minimums are 3, 1, 2, 4, 1, 1, 2, 1, 1, 1.  Sum is 17.
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# 思路：
# 首先构造一个monotone stack/queue:
# monotone stack/queue 的定义：一直是decreasing 或者increasing
# “栈内元素按单调递增或单调递减来排列”
#  这一题我们要找到，这个元素之后最小的元素，所以是个decreasing monotenic queue
#       对于A里每个数：push index instead of the number 
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
from collections import deque
class Solution:
    def sumSubarrayMins(self, A: List[int]) -> int:
# 首先构造一个monotone stack/queue:
# monotone stack/queue 的定义：一直是decreasing 或者increasing
# “栈内元素按单调递增或单调递减来排列”
#  这一题我们要找到，这个元素之后最小的元素，所以是个decreasing monotenic queue
#       对于A里每个数：push index instead of the number 
        left,m_queue = [-1] * len(A), []
        for i in range(len(A)):
            
            while m_queue and A[m_queue[-1]]>A[i]:
                m_queue.pop()
            if not m_queue:
                left[i] = -1
            else:
                left[i] =m_queue[-1]
            m_queue.append(i)
        for i in range(len(A)):
            left[i] =  i+1 if left[i] == -1 else i - left[i]
            
        m_queue = []
        right,m_queue = [-1] * len(A), []
        for i in range(len(A)):
            while m_queue and A[m_queue[-1]]>A[i]:
                right[m_queue.pop()] = i
            m_queue.append(i)
        for i in range(len(A)):
            right[i] =  len(A) - i if right[i] == -1 else right[i] - i
#       For example, in this test where input is [3,1,2,4]
#       We will have 
#       PLE = [-1, 3, 3, -1]
#       NLE = [3, 3, 3, -1]
#       对于A中的每一个数，包含其的subarray+ 并且它是里面最小的数的次数
#       = A[i] 到 previous less number 的距离* A[i] 到next less number 的距离 （组合）
        
        mod =  (10**9) + 7
        return sum(a*l*r for a,l,r in zip(A, left, right)) % mod
            
        