class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        seen = {}
        res = 0
        for r, c in enumerate(s):
            while c in seen:
                seen.pop(s[l])
                l += 1
            seen[c] = 1
            res = max(res, r-l+1)

        return res
