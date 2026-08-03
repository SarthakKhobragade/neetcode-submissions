class Solution:
    def rob(self, nums: List[int]) -> int:
        size = len(nums)
        if size <= 2:
            return max(nums)
    
        robbed = [0] * size
        robbed[0] = nums[0]
        robbed[1] = max(nums[0],nums[1])

        for i in range(2, size):
            robbed[i] = max(robbed[i-1], nums[i] + robbed[i-2])
        
        return robbed[-1]