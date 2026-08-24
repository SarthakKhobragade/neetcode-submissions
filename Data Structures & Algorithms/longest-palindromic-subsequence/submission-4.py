class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        memo = {}

        def find(i, j):
            if i > j:
                return 0
            if i == j:
                return 1
            if (i,j) in memo:
                return memo[(i,j)]

            if s[i] == s[j]:
                memo[(i, j)] = 2 + find(i + 1, j - 1)
                return memo[(i, j)]

            memo[(i, j)] = max(find(i, j - 1), find(i + 1, j))
            return memo[(i, j)]

        return find(0, len(s) - 1)
