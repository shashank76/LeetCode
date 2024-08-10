class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        rows, cols = len(grid), len(grid[0])
        rows2, cols2 = 3*rows, 3*cols
        grid2=[[0]*cols2 for _ in range(rows2)]
        
        
        for r in range(rows):
            for c in range(cols):
                r2, c2 = r*3, c*3
                if grid[r][c] == "/":
                    grid2[r2][c2+2] = 1
                    grid2[r2+1][c2+1]=1
                    grid2[r2+2][c2]=1
                elif grid[r][c] == "\\":
                    grid2[r2][c2] = 1
                    grid2[r2+1][c2+1]=1
                    grid2[r2+2][c2+2]=1
                
        def dfs(r, c, visited):
            if (r < 0 or c < 0 or r == rows2 or c == cols2 or 
                grid2[r][c] != 0 or (r,c) in visited):
                return 
            visited.add((r,c))
            adjs= [[r+1,c], [r,c+1], [r-1,c], [r,c-1]]
            for nr, nc in adjs:
                dfs(nr, nc, visited)
                
        visited = set()
        out = 0
        for r in range(rows2):
            for c in range(cols2):
                if grid2[r][c] == 0 and (r,c) not in visited:
                    dfs(r,c, visited)
                    out+=1
        return out
            
                
            