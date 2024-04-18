class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        visited = set()
        rows, cols = len(grid), len(grid[0])
        
        def check_peri(i, j):
            if i < 0 or j < 0 or i >= rows or j >= cols or grid[i][j] == 0:
                return 1
            if (i, j) in visited:
                return 0
            
            visited.add((i, j))
            count = check_peri(i, j-1)
            count += check_peri(i, j+1)
            count += check_peri(i-1, j)
            count += check_peri(i+1, j)
            
            return count
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]:
                    return check_peri(i, j)        