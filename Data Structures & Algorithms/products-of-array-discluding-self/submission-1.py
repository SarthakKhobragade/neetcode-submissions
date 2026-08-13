class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        size = len(nums)
        prefix = [1] * (size+1)
        suffix = [1] * (size+1)


        for i in range(size):
            prefix[i] = prefix[i-1] * nums[i]
            suffix[size-i-1] = suffix[(size-i)% size] * nums[size-i-1]
        

        res = []

        for i in range(size):
            val = prefix[i-1] * suffix[i+1]
            res.append(val)
        
        return res