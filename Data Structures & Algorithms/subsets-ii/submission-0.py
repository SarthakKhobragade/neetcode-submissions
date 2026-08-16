class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        nums.sort()

        def subsets(i, curr):
            if i >= len(nums):
                if curr not in res:
                    res.append(curr.copy())
                return
            
            curr.append(nums[i])
            subsets(i+1,curr)
            curr.pop()
            subsets(i+1,curr)
        
        subsets(0,[])
        return res
