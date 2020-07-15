# Tag: Binary Search + DP
# 975. Odd Even Jump
# -----------------------------------------------------------------------------------
# Description:
# You are given an integer array A.  From some starting index, you can make a series of jumps. 
#  The (1st, 3rd, 5th, ...) jumps in the series are called odd numbered jumps,
#  and the (2nd, 4th, 6th, ...) jumps in the series are called even numbered jumps.

# You may from index i jump forward to index j (with i < j) in the following way:

# During odd numbered jumps (ie. jumps 1, 3, 5, ...), you jump to the index j such that 
# A[i] <= A[j] and A[j] is the smallest possible value.  If there are multiple such indexes j,
#  you can only jump to the smallest such index j.
# During even numbered jumps (ie. jumps 2, 4, 6, ...), you jump to the index j such that
#  A[i] >= A[j] and A[j] is the largest possible value.  If there are multiple such indexes j, 
# you can only jump to the smallest such index j.
# (It may be the case that for some index i, there are no legal jumps.)
# A starting index is good if, starting from that index, you can reach the end of the array (index A.length - 1) by jumping some number of times (possibly 0 or more than once.)

# Return the number of good starting indexes.
# -----------------------------------------------------------------------------------
# Example:
# Input: [10,13,12,14,15]
# Output: 2
# Explanation: 
# From starting index i = 0, we can jump to i = 2 (since A[2] is 
# the smallest among A[1], A[2], A[3], A[4] that is greater or equal to A[0]),
#  then we can't jump any more.
# From starting index i = 1 and i = 2, we can jump to i = 3, then we can't jump any more.
# From starting index i = 3, we can jump to i = 4, so we've reached the end.
# From starting index i = 4, we've reached the end already.
# In total, there are 2 different starting indexes (i = 3, i = 4) where we can 
# reach the end with some number of jumps.
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# 思路：
# 如果是奇数次jump -＞ 下一个数是比curr num 大最小的数
# 如果是偶数次jump -＞ 下一个数是比curr num 小最大的数
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
class Solution:
    def oddEvenJumps(self, A: List[int]) -> int:
        count = 1
        n = len(A)-1
        hashmap_odd = {x:[]for x in range(n)}
        hashmap_even = {x:[]for x in range(n)}
#       Starting from index A[0] to index A[n-1]
#       For every starting index, always start from 1st jump
        # 在想可以搞个hashmap 然后，把每个数能不能reach end 都存起来
        def searchSmallest(num,A_StoL):
            for i in range(len(A_StoL)):
#               Return 第一个比num大的数，因l是从小到大排序
                if A_StoL[i] > num:
                    return A_StoL[i]
        def searchLargest(num):
            for i in range(len(A_LtoS)):
#               Return 第一个比num小的数，因l是从大到小排序
                if A_LtoS < num:
                    return A_LtoS[i]
        def canreach(ind,jump):
            num = A[ind]
            sub= A[ind+1:]
            if not sub:
                return 
            sub.sort()
#           如果是odd jump ->找比num大的最小的数
            if jump %2 != 0:
                if hashmap_odd[ind]:
                    return hashmap_odd[ind]
                else:
                    if num < sub[-1] :
                        next_number = searchSmallest(num,sub)
                        hashmap_odd[ind].append(A.index(next_number))
                        hashmap_odd[ind].append(canreach(A.index(next_number),jump+1))
                        hashmap_even[ind].append(None)
                    else:
                        return
            #如果是even jump->找比num小最大的数
            if jump %2 == 0:
                if hashmap_even[ind]:
                    return hashmap_even[ind]
                else:
                    if num > sub[0]:
                        next_number = searchSmallest(num,sub[::-1])
                        hashmap_even[ind].append(A.index(next_number))
                        hashmap_even[ind].append(canreach(A.index(next_number),jump+1))
                    else:
                        hashmap_even[ind].append(None)
                        return 
            
            
#       一直loop直到填满了hashmap
        for i in range(n):
            jump = 1
            canreach(i,jump)
        ans = []
        for i in range(n):
            res = []
            jump = 1
            while jump < n:
                if jump % 2 !=0: #odd
                    if not hashmap_odd[i][0]:
                        break
                    elif hashmap_odd[i][0]:
                        res.append(hashmap_odd[i][0])
                        jump +=1
                elif jump % 2 ==0: #even
                    if not hashmap_even[i][0]:
                        break
                    elif hashmap_even[i][0]:
                        res.append(hashmap_even[i][0])
                        jump +=1
            ans.append(res)
        for item in ans:
            if n in item:
                count +=1
        return hashmap_odd
