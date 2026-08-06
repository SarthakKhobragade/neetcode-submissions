class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        curr = 0
        size = float("inf")
        for r in range(len(nums)):
            curr += nums[r]
            while curr >= target:
                size = min(size, r - l + 1)
                curr -= nums[l]
                l += 1
        
        return size if size != float("inf") else 0