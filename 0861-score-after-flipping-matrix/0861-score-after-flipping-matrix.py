class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        def flipRow(r):
            for c in range(cols):
                grid[r][c] = 1 - grid[r][c] 

        def flipCol(c):
            for r in range(rows):
                grid[r][c] = 1 - grid[r][c]

        def checkRow(nums):
            return int(''.join([str(n) for n in nums]), 2)
        
        for r in range(rows):
            if grid[r][0] == 0:
                flipRow(r)
        
        for c in range(1, cols):
            if sum(grid[r][c] for r in range(rows)) * 2 < rows:
                flipCol(c)
        
        return sum(checkRow(r) for r in grid)
