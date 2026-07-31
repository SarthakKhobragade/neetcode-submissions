class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] != 0:
            return -1
        dist = [float("inf")]
        visited = set([(0, 0)])
        rows, cols = len(grid), len(grid[0])
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        queue = deque([])
        queue.append((0, 0, 1))

        def bfs():
            while queue:
                size = len(queue)
                for _ in range(size):
                    r, c, curr = queue.popleft()
                    if (r, c) == (rows - 1, cols - 1):
                        dist[0] = min(dist[0], curr)
                        return
                    for dr, dc in directions:
                        nr, nc = dr + r, dc + c
                        if (
                            nr in range(rows)
                            and nc in range(cols)
                            and grid[nr][nc] == 0
                            and (nr, nc) not in visited
                        ):
                            visited.add((nr, nc))
                            queue.append((nr, nc, curr + 1))

        bfs()
        return dist[0] if dist[0] != float("inf") else -1