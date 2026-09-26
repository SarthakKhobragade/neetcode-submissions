class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        for i in range(1, len(prices)):
            prev = prices[i-1]
            curr = prices[i]

            diff = curr - prev
            if diff >= 0:
                res += diff
        
        return res