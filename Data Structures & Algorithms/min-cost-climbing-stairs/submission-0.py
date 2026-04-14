class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        copy = [0] * (n + 1)

        for i in range(2, n + 1):
            copy[i] = min(copy[i-1] + cost[i-1], copy[i - 2] + cost[i - 2])
        return copy[-1]
        

        