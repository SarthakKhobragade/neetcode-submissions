class Solution:
    def maximumProfit(self, profits: List[int], weights: List[int], capacity: int) -> int:
        memo = {}

        def find(i, cap):
            if cap < 0:
                return -1e9

            if i == len(profits):
                return 0
            if (i, cap) in memo:
                return memo[(i, cap)]

            pick = profits[i] + find(i + 1, cap - weights[i])
            not_pick = 0 + find(i + 1, cap)

            memo[(i, cap)] = max(pick, not_pick)
            return memo[(i, cap)]

        max_profit = find(0, capacity)
        return max_profit
