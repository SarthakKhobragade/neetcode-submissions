class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[-1][-1] == 1 or obstacleGrid[0][0]:
            return 0

        rows, cols = len(obstacleGrid), len(obstacleGrid[0])
        grid = [[0]* (cols+1) for _ in range(rows+1)]

        grid[rows-1][cols-1] = 1

        for r in range(rows-1,-1,-1):
            for c in range(cols-1,-1,-1):
                if (r,c) == (rows-1,cols-1):
                    continue
                if obstacleGrid[r][c] == 1:
                    grid[r][c] = 0
                else:
                    grid[r][c] = grid[r+1][c] + grid[r][c+1]

        return grid[0][0]