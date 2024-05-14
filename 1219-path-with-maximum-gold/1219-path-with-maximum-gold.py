class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        def findMaxGold(x,y):
            temp = grid[x][y]
            dir = [(-1,0),(1,0),(0,1),(0,-1)]
            grid[x][y]=0
            out = temp
            for i,j in dir:
                if (0 <= x + i < rows and 0 <= y + j < cols and grid[x+i][y+j]) > 0:
                    out=max(out, temp + findMaxGold(x+i, y+j))
            grid[x][y] = temp
            return out

        out = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==0:
                    continue
                out= max(out, findMaxGold(r,c))
        
        return out