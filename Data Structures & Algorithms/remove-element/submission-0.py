class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        curr = []

        for num in nums:
            if num != val:
                curr.append(num)

        for i, num in enumerate(curr):
            nums[i] = curr[i]
        
        return len(curr)

        