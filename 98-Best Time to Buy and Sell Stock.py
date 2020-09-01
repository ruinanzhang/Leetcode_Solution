# Tag: Array 
# 121. Best Time to Buy and Sell Stock
# -----------------------------------------------------------------------------------
# Description: 

# Say you have an array for which the ith element is the price of a given stock on day i.

# If you were only permitted to complete at most one transaction (i.e., buy one and sell
#  one share of the stock), design an algorithm to find the maximum profit.

# Note that you cannot sell a stock before you buy one.
# -----------------------------------------------------------------------------------
# Example 1:

# Input: [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Not 7-1 = 6, as selling price needs to be larger than buying price.

# Example 2:
# Input: "226"
# Output: 3
# Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# 思路：
# Initial thoughts, use matrix to calculate the difference of value i,j 
# Will be n^2
# One path, to check the max_profit accordingly to the min_price
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        n = len(prices)
        min_price = prices[0]
        max_profit = 0
        for i in range(n):
            if prices[i] < min_price:
                min_price = prices[i]
            elif prices[i] - min_price > max_profit:
                max_profit = prices[i] - min_price
        return max_profit
                