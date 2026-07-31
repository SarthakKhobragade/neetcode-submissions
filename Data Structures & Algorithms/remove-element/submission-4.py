class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        size = len(nums)
        left = 0
        right = size - 1
        count = 0

        while left < right and left < size:
            while right > 0 and nums[right] == val:
                right -= 1
            
            if nums[left] == val:
                count += 1
                nums[left], nums[right] = nums[right], nums[left]
            left += 1

        return size - nums.count(val)