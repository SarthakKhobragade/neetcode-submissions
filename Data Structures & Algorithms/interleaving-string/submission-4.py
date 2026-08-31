class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        rows, cols = len(s1), len(s2)
        if len(s3) != rows + cols:
            return False

        dp = [[False] * (cols+1) for _ in range(rows+1)]

        dp[rows][cols] = True

        for i in range(rows,-1,-1):
            for j in range(cols,-1,-1):
                if i == rows and j == cols:
                    continue
                option1 = False
                if i < rows and s1[i] == s3[i + j]:
                    option1 = dp[i + 1][j]

                option2 = False
                if j < cols and s2[j] == s3[i + j]:
                    option2 = dp[i][j + 1]

                dp[i][j] = option1 or option2
        
        return dp[0][0]