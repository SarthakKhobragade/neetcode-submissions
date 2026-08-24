class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        rows = len(text1)
        cols = len(text2)
        res = [[0] * (cols+1) for _ in range(rows + 1)]

        for i in range(rows-1,-1,-1):
            for j in range(cols-1,-1,-1):
                if text1[i] == text2[j]:
                    res[i][j] = 1 + res[i+1][j+1]
                else:
                    res[i][j] = max(res[i+1][j], res[i][j+1])

        return res[0][0]
