class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        size = len(nums)
        prefix = [0] * (size+1)

        for i in range(size):
            prefix[i] = prefix[i-1] + nums[i]

        seen = {0:1}

        res = 0
        for i in range(size):
            res += seen.get(prefix[i]-k,0)
            seen[prefix[i]] = 1 + seen.get(prefix[i],0)

        return res 
