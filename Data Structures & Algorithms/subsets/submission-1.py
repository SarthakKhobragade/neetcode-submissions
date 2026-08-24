class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def find(i, curr):
            if i == len(nums):
                res.append(curr.copy())
                return
            
            curr.append(nums[i])
            find(i+1,curr)
            curr.pop()
            find(i+1,curr)

        find(0, [])
        return res