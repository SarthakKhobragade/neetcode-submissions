class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        size = len(prices)
        profit = 0
        for i in range(size):
            for j in range(i+1, size):
                diff = prices[j]-prices[i]
                profit = max(profit, diff)
        
        return profit