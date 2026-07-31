class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        directions= [(0,1), (0,-1), (1,0),(-1,0)]

        visited = set()

        rows, cols = len(image), len(image[0])

        def fill(r,c, change):
            if r not in range(rows) or c not in range(cols) or (r,c) in visited or image[r][c] != change:
                return
            visited.add((r,c))
            image[r][c] = color
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                fill(nr, nc, change)

        change = image[sr][sc]
        fill(sr, sc, change)
        return image
