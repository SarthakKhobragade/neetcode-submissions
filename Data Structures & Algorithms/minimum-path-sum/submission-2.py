class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        for i in range(rows-1,-1,-1):
            for j in range(cols-1,-1,-1):
                if i == rows - 1 and j == cols - 1:
                    continue
                down = grid[i+1][j] if i + 1 in range(rows) else 1e9
                right = grid[i][j+1] if j + 1 in range(cols) else 1e9
                grid[i][j] = grid[i][j] + min(down, right)
            
        return grid[0][0]