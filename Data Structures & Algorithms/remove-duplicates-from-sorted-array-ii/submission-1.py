class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return len(nums)
        l = 1
        count = 1
        for r in range(1, len(nums)):
            if nums[r] == nums[r-1] and count < 2:
                l += 1
                count +=1
                continue
            if nums[r] != nums[r-1]:
                count = 1
                for j in range(l,r):    
                    nums[j] = nums[r]
                l += 1
        return l


