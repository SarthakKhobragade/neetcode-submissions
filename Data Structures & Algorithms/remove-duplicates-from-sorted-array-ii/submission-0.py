class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        seen = {}

        for num in nums:
            if num in seen and seen[num] >= 2:
                continue
            seen[num] = 1 + seen.get(num, 0)
        
        i = 0
        for key,val in seen.items():
            for _ in range(val):
                nums[i] = key
                i += 1
        
        return i

        
