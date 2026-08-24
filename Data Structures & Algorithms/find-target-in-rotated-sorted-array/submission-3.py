class Solution:
    def search(self, nums: List[int], target: int) -> int:
        size = len(nums)
        l, r = 0, size - 1

        while l < r:
            mid = (l + r) // 2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid

        split = l

        if split == 0:
            l, r = 0, size - 1
        else:
            if nums[0] <= target <= nums[split - 1]:
                l, r = 0, split - 1
            else:
                l, r = split, size - 1

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1

        return -1
