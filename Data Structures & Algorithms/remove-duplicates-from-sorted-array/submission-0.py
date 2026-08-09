class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        res = []
        seen = set()
        for num in nums:
            if num not in seen:
                seen.add(num)
                res.append(num)
        
        for i,num in enumerate(res):
            nums[i] = num
        
        return len(res)

