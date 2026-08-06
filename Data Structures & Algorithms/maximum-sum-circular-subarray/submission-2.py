class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        max_sum = nums[0]
        curr_sum = 0
        for num in nums:
            curr_sum = max(curr_sum, 0)
            curr_sum += num
            max_sum = max(max_sum, curr_sum)

        min_sum = nums[0]
        curr_sum = 0
        for num in nums:
            curr_sum = min(curr_sum, 0)
            curr_sum += num
            min_sum = min(min_sum, curr_sum)
        
        if max_sum < 0:
            return max_sum
        return max(max_sum, sum(nums) - min_sum)