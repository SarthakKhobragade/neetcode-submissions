class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        size = len(prices)
        max_to_right = [0] * (size+1)
        max_profit = 0
        for i in range(size-1,-1,-1):
            max_to_right[i] = max(max_to_right[i+1], prices[i])

        for i, price in enumerate(prices):
            profit = max_to_right[i] - price
            max_profit = max(max_profit, profit)

        return max_profit