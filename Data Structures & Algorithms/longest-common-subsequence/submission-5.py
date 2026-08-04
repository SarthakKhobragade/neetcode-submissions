class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        size1 = len(text1)
        size2 = len(text2)
        if size1 == 0 or size2 == 0:
            return 0

        grid = [[0]*(size2+1) for _ in range(size1+1)]

        for i in range(size1-1,-1,-1):
            for j in range(size2-1,-1,-1):
                if text1[i] == text2[j]:
                    grid[i][j] = 1 + grid[i+1][j+1]
                else:
                    grid[i][j] = max(grid[i][j+1], grid[i+1][j])

        return grid[0][0]