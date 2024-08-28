class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        visited = set()
        rows, cols = len(grid1), len(grid1[0])
        def dfs(i, j, grid):
            
            
            if 0 <= i < rows and 0 <= j < cols and (i, j) not in visited and grid[i][j] == 1:
                visited.add((i, j))
                grid[i][j] = 2
                dfs(i+1, j, grid)
                dfs(i-1, j, grid)
                dfs(i, j+1, grid)
                dfs(i, j-1, grid)
                
        for i in range(rows):
            for j in range(cols):
                if grid1[i][j]:
                    dfs(i, j, grid1)
        
        res = 0
        for i in range(rows):
            for j in range(cols):
                if grid2[i][j] == 1:
                    visited = set()
                    dfs(i, j, grid2)
                    if all(grid1[a][b] == 2 for a, b in visited):
                        res += 1
        return res
        