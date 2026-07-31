class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        def dfs(r, c):
            # Mark current cell visited and count it
            visited.add((r, c))
            area = 1
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (
                    0 <= nr < rows and 0 <= nc < cols
                    and (nr, nc) not in visited
                    and grid[nr][nc] == 1
                ):
                    area += dfs(nr, nc)
            return area

        max_area = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visited:
                    max_area = max(max_area, dfs(r, c))
        return max_area