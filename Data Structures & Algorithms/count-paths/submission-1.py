class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        rows, cols = m, n
        cache = {}
        def find_path(r,c):
            if r not in range(rows) or c not in range(cols):
                return 0
            if (r,c) == (rows-1, cols-1):
                return 1
            
            if (r,c) in cache:
                return cache[(r,c)] 

            right = find_path(r, c+1)
            down = find_path(r+1,c)

            cache[(r,c)] = right + down
            return cache[(r,c)] 
    

        return find_path(0,0)