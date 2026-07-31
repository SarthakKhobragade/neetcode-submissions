class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {}
        def count(curr):
            if curr in cache:
                return cache[curr]
            if curr <= 1:
                return 1

            val = count(curr-1)
            cache[curr-1] = val 
            val2 = count(curr-2)
            cache[curr-2] = val2
            return val + val2
        
        return count(n)
