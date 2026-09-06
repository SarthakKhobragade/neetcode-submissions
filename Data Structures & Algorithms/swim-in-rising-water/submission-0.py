class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def can_reach(t: int) -> bool:
            if grid[0][0] > t:
                return False

            queue = deque([(0, 0)])
            visited = {(0, 0)}
            while queue:
                r, c = queue.popleft()
                if r == n - 1 and c == n - 1:
                    return True

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (0 <= nr < n and 0 <= nc < n and (nr, nc) not in visited and grid[nr][nc] <= t):
                        visited.add((nr, nc))
                        queue.append((nr, nc))

            return False

        left = min(min(row) for row in grid)
        right = max(max(row) for row in grid)
        ans = right

        while left <= right:
            mid = (left + right) // 2
            if can_reach(mid):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1

        return ans