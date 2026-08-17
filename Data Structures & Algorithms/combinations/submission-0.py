class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = [x for x in range(1, n + 1)]

        res = []

        def backtrack(i, curr):
            if len(curr) >= k:
                res.append(curr.copy())
                return
            if i >= len(nums):
                return

            curr.append(nums[i])
            backtrack(i + 1, curr)
            curr.pop()
            backtrack(i + 1, curr)

        backtrack(0, [])
        return res
