class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[-1][-1] == 1 or obstacleGrid[0][0]:
            return 0
        cache = {}
        rows, cols = len(obstacleGrid), len(obstacleGrid[0])

        def find_path(r, c):
            if r >= rows or c >= cols or obstacleGrid[r][c] == 1:
                return 0

            if (r, c) == (rows - 1, cols - 1):
                return 1

            if (r,c) in cache:
                return cache[(r,c)]

            down = find_path(r + 1, c)
            right = find_path(r, c + 1)
            cache[(r,c)] = down+right
            return cache[(r,c)]

        return find_path(0,0)
