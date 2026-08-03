class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 1:
            return 1
        prev = 0
        curr = 1

        res = 0

        while n:
            res = prev + curr
            prev = curr
            curr = res
            n -= 1
    
        return res