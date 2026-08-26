class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        memo = {}
        def find(i, curr):
            if (i,curr) in memo:
                return memo[(i,curr)]
            if curr > total/2:
                return False
            if curr == total/2:
                return True
            if i == len(nums):
                return False
            
            pick = find(i+1, curr + nums[i])
            not_pick = find(i+1, curr)

            memo[(i,curr)] = pick or not_pick
            return memo[(i,curr)]

        
        return find(0, 0)