class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        size = len(nums)
        res = [1] * size
        prefix = 1
        suffix = 1

        # Store the product of all elements to the left
        prefix = 1
        for i in range(size):
            res[i] = prefix * res[i]
            prefix = prefix * nums[i]

        # Multiply by the product of all elements to the right
        suffix = 1
        for i in range(size - 1, -1, -1):
            res[i] = res[i] * suffix
            suffix = suffix * nums[i]

        return res