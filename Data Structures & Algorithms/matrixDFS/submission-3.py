class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        count = [0]
        rows, cols = len(grid),len(grid[0])
        visited = set()
        if grid[0][0] == 1:
            return 0
        visited.add((0,0))
        directions = [(0,1),(0,-1),(1,0),(-1,0)]

        def dfs(r,c):
            if (r,c) == (rows-1,cols-1):
                count[0] += 1
                return
            
            for dr,dc in directions:
                nr,nc = dr+r,dc+c
                if nr in range(rows) and nc in range(cols) and grid[nr][nc] == 0 and (nr,nc) not in visited:
                    visited.add((nr,nc))
                    dfs(nr,nc)
                    visited.remove((nr,nc))


        dfs(0,0)
        return count[0]