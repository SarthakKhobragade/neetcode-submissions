class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        def dfs(r, c):
            # Base case: invalid cell (out of bounds, water, or already visited)
            if (r < 0 or r >= rows or c < 0 or c >= cols 
                or grid[r][c] == 0 or (r, c) in visited):
                return 0
            
            # Mark visited and count this cell
            visited.add((r, c))
            area = 1
            
            # Explore all four directions
            for dr, dc in directions:
                area += dfs(r + dr, c + dc)
            
            return area

        max_area = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visited:
                    max_area = max(max_area, dfs(r, c))
        return max_area