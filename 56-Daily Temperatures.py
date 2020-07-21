# Tag: Monotonic Stack
# 739. Daily Temperatures
# -----------------------------------------------------------------------------------
# Description:
# Given a list of daily temperatures T, return a list such that, for each day in the input,
#  tells you how many days you would have to wait until a warmer temperature. 
# If there is no future day for which this is possible, put 0 instead.
# -----------------------------------------------------------------------------------
# For example, given the list of temperatures T = [73, 74, 75, 71, 69, 72, 76, 73],
#  your output should be [1, 1, 4, 2, 1, 1, 0, 0].
# -----------------------------------------------------------------------------------
# Note:
# The length of temperatures will be in the range [1, 30000].
# Each temperature will be an integer in the range [30, 100].
# -----------------------------------------------------------------------------------
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# 思路：
#   这道题说白了就是找到Next larger number -》（递减）
#   想到用递减monotonic stakc + reverse the list 来做
#   递减是->每个数会把比它大的踢出去
#   monotonic stack的精髓就是在于pop出去的时候（出栈计算很重要！！）
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        mono_stack = []
        re_T = T[::-1]
        # 在这里在tail加一个101（因为最大温度100），保证了stack所有数都会被pop
        re_T.append(101)
        res = [0 for x in range(len(re_T))]
        for i in range(len(re_T)):
#           In mono_stack, we store index
            while mono_stack and re_T[i] >=re_T[mono_stack[-1]]:
                poped_ind = mono_stack.pop()
                if not mono_stack:
                    res[poped_ind] = 0
                else:
                    res[poped_ind] = poped_ind - mono_stack[-1]
            mono_stack.append(i)
        res.pop()
        return res[::-1]
