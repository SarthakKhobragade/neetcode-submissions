class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        dp = {0}  # A set containing just the number 0
        target = sum(nums)/2

        for i in range(len(nums)): 
            next_dp = set() 
            for val in dp: 
                next_dp.add(val + nums[i])
                next_dp.add(val)
            dp = next_dp
            if target in dp:
                return True

        return False
