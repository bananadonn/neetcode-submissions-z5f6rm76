class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r = 0,1
        profit = 0
        
        for l in range(len(prices)):
            for r in range(l,len(prices)):
                profit = max(profit, prices[r] - prices[l])

        return profit
