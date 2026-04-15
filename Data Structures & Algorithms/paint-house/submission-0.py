class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        dp = [0] * len(costs[0])

        for cost in costs:
            r = dp[0]
            g = dp[1]
            b = dp[2]
            dp[0] = cost[0] + min(g, b)
            dp[1] = cost[1] + min(r, b)
            dp[2] = cost[2] + min(r, g)
        
        return min(dp)
        
        