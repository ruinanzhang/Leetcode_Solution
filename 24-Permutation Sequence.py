# Tag: Recursion+Math+Backtracking
# 60. Permutation Sequence (LeetCode)
# -----------------------------------------------------------------------------------
# Description:
# The set [1,2,3,...,n] contains a total of n! unique permutations.
# By listing and labeling all of the permutations in order, 
# we get the following sequence for n = 3:
# "123"
# "132"
# "213"
# "231"
# "312"
# "321"
# Given n and k, return the kth permutation sequence.
# -----------------------------------------------------------------------------------
# Assumptions: 
#Given n will be between 1 and 9 inclusive.
# Given k will be between 1 and n! inclusive.
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# 思路： Index mapping + Recursion 
# 1. 首先，以n=3 为例子：一共可能的排列组合有(3)! = 3*2*1 = 6 种
# 1 "123"
# 2 "132"
# 3 "213"
# 4 "231"
# 5 "312"
# 6 "321"
# 2. 那么对于第一位数，我们决定的方法是：
# 如果第一位数确定，那么第一位数确定的排列组合有(3-1)! = 2 种，所以对于第一个数，每个数会重复出现2次
# 所以 用 k // 2 ，我们就知道第一个数是什么了 （这里有一个number List = [1,2,3]） qoutient 决定index
# ！！！！！！但要注意因为2//2=1 但其实我们还是在看第一个数，所以要用（k-1）//2
# 然后对于下一个k， k=reminder of k //2 which is k%2
# 就相当于除去第一个数，之后的数的循环。。。（难以解释啊！！！）
# 3. 既然知道第一位数的决定方法，后面就很简单了，只是因为数不会重复出现，所以更新我们的number List，
# 删除第一个数，然后recursvily 做step 2！
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        def getNthNum(ind,n,k,numList):
            reminder = 0
            re_num = 1
            for i in range(1,n-ind):
                re_num = i*re_num
            quotient = (k-1) // re_num
            reminder = k % re_num 
            ans = numList[quotient]
            k = reminder
            numList.remove(ans)
            return str(ans),k
        numList = []
        for x in range(1,n+1):
            numList.append(x)
        res = ""
        for ind in range(0,n):    
            string,k= getNthNum(ind,n,k,numList)
            res = res + string
        return res
                   
        
                
                
        
        