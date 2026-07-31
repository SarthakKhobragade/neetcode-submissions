class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = {}

        for num in nums:
            count[num] = 1 + count.get(num, 0)

        pos = 0
        for i in range(3):
            while i in count and count[i] > 0:
                nums[pos] = i
                count[i] -= 1
                pos += 1
        
        return nums

        