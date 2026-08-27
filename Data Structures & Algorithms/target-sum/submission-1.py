class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        size = len(nums)
        memo = {}
        def find(i, curr):
            if i == size:
                if curr == target:
                    return 1
                return 0

            if (i,curr) in memo:
                return  memo[(i, curr)]

            memo[(i, curr)] = find(i +1 , curr + nums[i]) + find(i+1, curr - nums[i])

            return  memo[(i, curr)] 
        res = find(0,0)
        return res