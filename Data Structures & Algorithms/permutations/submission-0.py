class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        taken = {num:False for num in nums}

        def find(curr):
            if len(curr) == len(nums):
                res.append(curr.copy())
                return

            for num in nums:
                if not taken[num]:
                    taken[num] = True
                    curr.append(num)
                    find(curr)
                    curr.pop()
                    taken[num] = False
                
        find([])
        return res