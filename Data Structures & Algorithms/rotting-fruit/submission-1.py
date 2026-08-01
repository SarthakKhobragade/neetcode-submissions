class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        queue = deque([])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = set()
        min_time = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c, 0))

        while queue:
            r, c, time = queue.popleft()
            min_time = max(min_time, time)
            for dr, dc in directions:
                nr, nc = dr + r, dc + c
                if nr in range(rows) and nc in range(cols) and grid[nr][nc] == 1 and (nr,nc) not in visited:
                    visited.add((nr,nc))
                    grid[nr][nc] = 2
                    queue.append((nr,nc, time+1))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    return -1

        return min_time