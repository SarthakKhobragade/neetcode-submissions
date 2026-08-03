class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = {}
        def f(i):
            if i >= len(nums):
                return 0
            if i in cache:
                return cache[i]
            cache[i] = max(nums[i]+ f(i+2),f(i+1))
            return cache[i]

        return f(0)
