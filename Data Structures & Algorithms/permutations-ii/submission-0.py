class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = set()
        visited = set()
        def find(curr):
            if len(curr) == len(nums):
                res.add(tuple(curr.copy()))
                return

            for i in range(len(nums)):
                if i not in visited:
                    visited.add(i)
                    curr.append(nums[i])
                    find(curr)
                    curr.pop()
                    visited.remove(i)
            
        find([])

        return list(res)