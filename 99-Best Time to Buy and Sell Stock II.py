# Tag:DP
# 322. Coin Change
# -----------------------------------------------------------------------------------
# Description: 
# You are given coins of different denominations and a total amount of money amount.
# Write a function to compute the fewest number of coins that you need to make up 
# that amount. If that amount of money cannot be made up by any combination of the coins, return -1.
# -----------------------------------------------------------------------------------
# Note:

# You may assume that you have an infinite number of each kind of coin.
# -----------------------------------------------------------------------------------
# Example 1:

# Input: coins = [1, 2, 5], amount = 11
# Output: 3 
# Explanation: 11 = 5 + 5 + 1
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# 思路：
# 和decode ways 类似，用backtrack会超时
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# Use DP, use backtracking will exceed time limt!!! 
# Base remain == 0 : return dp[amount]
# Limitation: remain <0: return -1 // can't find
# formula: dp[amount] = dp[amount-coin[i]] + 1


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount+1 for _ in range(amount+1)]
        # dp[i] defined as given amount i -> the number of fewest number of coins
        # need to make up the amount 
        dp[0] = 0
        for i in range(1,len(dp)): 
            for coin in coins:
                if i-coin<0:
                    continue
                dp[i] = min(dp[i], dp[i-coin] + 1)
        if dp[amount] == amount+1:
            return -1
        return dp[amount]