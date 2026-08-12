class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        size = len(nums)
        prefix = [0] * (size+1)
        suffix = [0] * (size+1)

        for i in range(size):
            prefix[i] = prefix[i-1] + nums[i]
            suffix[size-i-1] = suffix[(size-i)%size] + nums[size-i-1]

        for i in range(size):
            if prefix[i-1] == suffix[i+1]:
                return i
        
        return -1

        