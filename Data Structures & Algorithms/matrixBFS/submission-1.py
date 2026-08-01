class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid),len(grid[0])
        if not grid or grid[0][0] == 1:
            return -1

        queue = deque([])
        queue.append((0,0,0))
        visited = set()
        visited.add((0,0))
        directions = [(0,1),(0,-1),(1,0),(-1,0)]

        def bfs(r,c):
            while queue:
                r,c, dist = queue.popleft()
                if (r,c) == (rows-1,cols-1):
                    return dist

                for dr,dc in directions:
                    nr,nc = dr+r,dc+c
                    if nr in range(rows) and nc in range(cols) and grid[nr][nc] == 0 and (nr,nc) not in visited:
                        visited.add((nr,nc))
                        queue.append((nr,nc, dist+1))
            return -1

        dist = bfs(0,0)
        return dist