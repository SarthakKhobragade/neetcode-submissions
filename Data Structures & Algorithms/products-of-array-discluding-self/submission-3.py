class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        size = len(nums)
        res = [1] * size
        prefix = 1
        suffix = 1

        for i in range(size):
            res[i] *= prefix
            res[size - 1 - i] *= suffix
            prefix *= nums[i]
            suffix *= nums[size - 1 - i]

        return res