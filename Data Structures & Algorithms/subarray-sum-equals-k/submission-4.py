class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        size = len(nums)
        prefix = [0] * (size+1)

        for i in range(size):
            prefix[i] = prefix[i-1] + nums[i]

        seen = {}

        res = 0
        for i in range(size):
            if prefix[i] == k:
                res += 1
            res += seen.get(prefix[i]-k,0)
            seen[prefix[i]] = 1 + seen.get(prefix[i],0)

        return res 
