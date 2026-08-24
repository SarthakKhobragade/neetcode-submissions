class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        res = []

        def find(i, curr):
            if i == len(nums):
                res.append(curr.copy())
                return

            curr.append(nums[i])
            find(i + 1, curr)
            curr.pop()
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            find(i + 1, curr)

        find(0, [])
        return res
