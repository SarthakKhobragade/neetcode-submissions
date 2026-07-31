class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        
        rows = len(matrix)
        cols = len(matrix[0])

        def matrix_index(mid):
            row = mid // cols
            col = mid % cols
            return row, col



        total = (rows * cols) - 1

        left, right = 0, total 

        while left < right:
            mid = (left+right)//2
            x,y = matrix_index(mid)
            if matrix[x][y] >= target:
                right = mid
            else:
                left = mid + 1
        
        x,y = matrix_index(left)

        return matrix[x][y] == target



