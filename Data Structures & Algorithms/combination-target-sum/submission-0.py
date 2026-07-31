class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        curr = []
        def find(curr, arr, i):
            if curr == target:
                result.append(arr.copy())
                return
            if i == len(nums) or curr > target:
                return

            arr.append(nums[i])
            find(curr+nums[i], arr, i)
            arr.pop()

            find(curr, arr, i+1)


        find(0, [], 0)
        return result