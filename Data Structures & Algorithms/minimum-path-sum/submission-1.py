class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        memo = {}
        def find(i, j):
            if i == len(grid) - 1 and j == len(grid[0]) - 1:
                return grid[i][j]
            if i == len(grid) or j == len(grid[0]):
                return float('inf')
            if (i,j) in memo:
                return memo[(i,j)]

            memo[(i,j)] = grid[i][j] + min(find(i + 1, j),find(i, j + 1))
            return memo[(i,j)]
        return find(0, 0)
