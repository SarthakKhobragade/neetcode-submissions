class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def build(i, curr):
            if i == len(nums):
                result.append(curr[::])
                return

            curr.append(nums[i])
            build(i+1, curr)
            curr.pop()
            build(i+1, curr)

        build(0, [])
        return result
