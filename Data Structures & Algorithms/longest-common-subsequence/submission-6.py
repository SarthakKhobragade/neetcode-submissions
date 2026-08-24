class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if len(text1) < len(text2):
            text1, text2 = text2, text1

        memo = {}
        def find(i, j):
            if i == len(text1) or j == len(text2):
                return 0
            if (i,j) in memo:
                return memo[(i,j)]
    
            if text1[i] == text2[j]:
                memo[(i,j)] = 1 + find(i + 1, j + 1)
                return memo[(i,j)]

            memo[(i,j)] = max(find(i + 1, j), find(i, j + 1))
            return memo[(i,j)]
        res = find(0, 0)
        return res