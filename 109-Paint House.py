# Tag: DP
# 256. Paint House
# -----------------------------------------------------------------------------------
# Description:
# There is a row of n houses, where each house can be painted one of three colors: 
# red, blue, or green. The cost of painting each house with a certain color is different.
#  You have to paint all the houses such that no two adjacent houses have the same color.

# The cost of painting each house with a certain color is represented by a n x 3 cost matrix. 
# For example, costs[0][0] is the cost of painting house 0 with the color red; costs[1][2] is 
# the cost of painting house 1 with color green, and so on... Find the minimum cost to paint all houses.
# -----------------------------------------------------------------------------------
# Examples:
# Example 1:
# Input: costs = [[17,2,17],[16,16,5],[14,3,19]]
# Output: 10
# Explanation: Paint house 0 into blue, paint house 1 into green, paint house 2 into blue.
# Minimum cost: 2 + 5 + 3 = 10.

# Example 2:
# Input: costs = []
# Output: 0
# -----------------------------------------------------------------------------------
# Note:
# costs.length == n
# costs[i].length == 3
# 0 <= n <= 100
# 1 <= costs[i][j] <= 20
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# 思路：
# DP Question 
# Paint_curr_r = mincost(paint_prev_green, paint_prev_blue) + cost_paint_curr_r
# dp[i][j] is the cost to paint current house i color j
# j -> red : 0 | blue: 1 | green : 2
# update dp[i][j] for every house i using rule:
# dp[i][0] = min (dp[i-1][1]. dp[i-1][2]) + costs[i][0]
# .....
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        if not costs:
            return 0
        n_color = len(costs[0])
        dp = [[0 for x in range(n_color)] for y in range(len(costs))]
        # dp[i][j] is the cost to paint current house i color j
        # j -> red : 0 | blue: 1 | green : 2
        # update dp[i][j] for every house i using rule:
        # dp[i][0] = min (dp[i-1][1]. dp[i-1][2]) + costs[i][0]
        # .....
        for i in range(len(costs)):
            for j in range(n_color):
                if i == 0:
                    dp[i][j] = costs[i][j]
                else:
                    dp[i][0] = min(dp[i-1][1],dp[i-1][2]) + costs[i][0]
                    dp[i][1] = min(dp[i-1][0],dp[i-1][2]) + costs[i][1]
                    dp[i][2] = min(dp[i-1][0],dp[i-1][1]) + costs[i][2]
        return min(dp[-1])