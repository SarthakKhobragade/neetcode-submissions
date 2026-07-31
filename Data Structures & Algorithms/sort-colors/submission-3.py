class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l, r = 0, len(nums) - 1
        pos = 0

        while pos <= r:
            if nums[pos] == 0:
                nums[l], nums[pos] = nums[pos],nums[l]
                l += 1
            elif nums[pos] == 2:
                nums[r], nums[pos] = nums[pos],nums[r]
                r -= 1
                pos -= 1
            pos += 1
