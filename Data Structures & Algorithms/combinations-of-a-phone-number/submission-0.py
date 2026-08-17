class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        nums = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        res = []
        def backtrack(i, curr):
            if len(curr) >= len(digits) and curr:
                res.append(''.join(curr))
                return
            if i >= len(digits):
                return

            for c in nums[digits[i]]:
                curr.append(c)
                backtrack(i+1, curr)
                curr.pop()

        backtrack(0, [])

        return res