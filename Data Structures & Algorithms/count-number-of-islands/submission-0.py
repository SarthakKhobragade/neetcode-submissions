class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()

        def dfs(r, c, visited):
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            for a, b in directions:
                r1 = r + a
                c1 = c + b

                if (
                    r1 in range(rows)
                    and c1 in range(cols)
                    and (r1, c1) not in visited
                    and grid[r1][c1] == "1"
                ):
                    visited.add((r1, c1))
                    dfs(r1, c1, visited)

        result = 0
        for r in range(rows):
            for c in range(cols):
                if (r, c) not in visited and grid[r][c] == "1":
                    dfs(r, c, visited)
                    result += 1
        
        return result
