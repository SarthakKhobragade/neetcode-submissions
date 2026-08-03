class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 1:
            return 1
        prev = 1
        curr = 1

        res = 0

        while n > 1:
            res = prev + curr
            prev = curr
            curr = res
            n -= 1
    
        return res