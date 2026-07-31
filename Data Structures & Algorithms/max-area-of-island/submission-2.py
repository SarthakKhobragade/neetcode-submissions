class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        max_area = 0
        
        def bfs(start_r, start_c):
            nonlocal max_area
            q = deque()
            q.append((start_r, start_c))
            visited.add((start_r, start_c))
            area = 0
            while q:
                r, c = q.popleft()
                area += 1
                for dr, dc in [(0,1),(0,-1),(1,0),(-1,0)]:
                    nr, nc = r+dr, c+dc
                    if (0 <= nr < ROWS and 0 <= nc < COLS and
                        (nr, nc) not in visited and grid[nr][nc] == 1):
                        visited.add((nr, nc))
                        q.append((nr, nc))
            max_area = max(max_area, area)   # update global after island is fully explored
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r, c) not in visited:
                    bfs(r, c)
        return max_area