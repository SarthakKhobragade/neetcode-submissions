class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        # memo = {}

        # def find(i, j):
        #     if i > j:
        #         return 0
        #     if i == j:
        #         return 1
        #     if (i,j) in memo:
        #         return memo[(i,j)]

        #     if s[i] == s[j]:
        #         memo[(i, j)] = 2 + find(i + 1, j - 1)
        #         return memo[(i, j)]

        #     memo[(i, j)] = max(find(i, j - 1), find(i + 1, j))
        #     return memo[(i, j)]

        # return find(0, len(s) - 1)
        rows, cols = len(s), len(s)
        res = [[0]*(cols+1) for _ in range(rows)]

        for i in range(rows-1,-1,-1):
            for j in range(i, cols):
                if i == j:
                    res[i][j] = 1
                    continue
                if s[i] == s[j]:
                    res[i][j] = res[i+1][j-1] + 2
                else:
                    res[i][j] = max(res[i+1][j], res[i][j-1])

        return res[0][cols-1]