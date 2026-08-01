class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        size = len(prices)
        buy = float("inf")
        max_profit = 0
        for price in prices:
            buy = min(buy, price)
            sell = price
            profit = sell - buy
            max_profit = max(max_profit, profit)

        return max_profit