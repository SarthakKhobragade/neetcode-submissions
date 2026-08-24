class Solution:
    def findMin(self, nums: List[int]) -> int:
        size = len(nums)
        l, r = 0, size - 1

        while l < r:
            mid = (l + r) // 2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        
        return nums[l]