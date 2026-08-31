class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        rows = len(word1)
        cols = len(word2)

        dp = [[0] * (cols+1) for _ in range(rows + 1)]

        for i in range(rows + 1):
            dp[i][cols] = rows - i

        for j in range(cols + 1):
            dp[rows][j] = cols - j

        for i in range(rows-1,-1,-1):
            for j in range(cols-1,-1,-1):
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i+1][j+1]
                else:
                    insert = 1 + dp[i][j+1]
                    delete = 1 + dp[i+1][j]
                    replace = 1 + dp[i+1][j+1]
                    dp[i][j] = min(insert, delete, replace)
        
        return dp[0][0]