# Tag: 2ptrs + Sliding Window❗️❗️❗️❗️❗️❗️❗️❗️❗️❗️❗️❗️❗️
# 904. Fruit Into Baskets Minimums
# -----------------------------------------------------------------------------------
# Description:
# In a row of trees, the i-th tree produces fruit with type tree[i].

# You start at any tree of your choice, then repeatedly perform the following steps:

# Add one piece of fruit from this tree to your baskets.  If you cannot, stop.
# Move to the next tree to the right of the current tree.  If there is no tree to the right, stop.
# Note that you do not have any choice after the initial choice of starting tree: you must perform step 1, 
# then step 2, then back to step 1, then step 2, and so on until you stop.

# You have two baskets, and each basket can carry any quantity of fruit, but you want each basket to only carry one type of fruit each.

# What is the total amount of fruit you can collect with this procedure?
# 简单来说就是含有两个元素的最长subarray～
# -----------------------------------------------------------------------------------
# Example 1:
#Input: [3,3,3,1,2,1,1,2,3,3,4]
# Output: 5
# Explanation: We can collect [1,2,1,1,2].
# If we started at the first tree or the eighth tree, we would only collect 4 fruits.
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
class Solution:
    def totalFruit(self, tree: List[int]) -> int:
#   思路：Intuitive thinking: iterate thru 
#   ！！！！！这里有一个重点！！如果看到type3的数，下一个数不用从第一个数看起了，直接从
#   type3之前的第一个type1的数开始check，因为中间的数肯定end to 第三个数
#   但如果只iterate-> get Time Limit Exceeded error 
#   于是用sliding window！！！
#   方法1: iterate 很慢！！！：
#   方法2:  2ptrs / Sliding Window
#       重点要想清楚的：这个sliding window只会因为能放下更多水果而增大，而不会缩小！！
#       记录最大basket的start ind -- max_start_ind
        max_start_ind = 0
#       这里用hashmap来写 basket
        basket = {}
#       记住这种用法：for key, value in list: (0,0),(1,1)(2,2)....
        for ind,value in enumerate(tree):
#           如果这是一种新水果：
            if value not in basket:
                basket[value] = 1
#           如果篮子里已经有这种水果：
            else: 
                basket[value]+=1
#           如果篮子里水果已经超过两周：
            if len(basket) > 2:
#               从最头上pop掉一个水果，但没必要变sliding window的长度，因为-1 +1 还是不变的
                basket[tree[max_start_ind]] -=1
#               如果某种水果已经全被pop完了，这个时候就需要删掉它，好让新的水果进来
                if basket[tree[max_start_ind]] == 0:
                    del basket[tree[max_start_ind]]
#               每次从前面pop掉一个水果，max_start_ind指针往后挪一个
                max_start_ind+=1
        return ind - max_start_ind +1  