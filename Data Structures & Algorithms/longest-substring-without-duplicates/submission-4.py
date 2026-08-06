class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        seen = {}
        res = 0
        for r in range(len(s)):
            while s[r] in seen:
                seen.pop(s[l])
                l += 1
            seen[s[r]] = 1
            res = max(res, r - l + 1)

        return res
