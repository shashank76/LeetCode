class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        time, fresh = 0, 0
        rows, cols = len(grid), len(grid[0])
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    fresh +=1
                if grid[i][j] == 2:
                    q.append([i, j])
        
        adjDir = [[0,1], [1,0], [0,-1], [-1,0]]
        
        while q and fresh >0:
            for i in range(len(q)):
                r, c = q.popleft()
                for x, y in adjDir:
                    row, col = r+x, c+y
                    if (row < 0 or row == rows or col < 0 or col == cols or 
                        grid[row][col] != 1):
                        continue
                    grid[row][col] = 2
                    fresh -=1
                    q.append([row, col])
            time+=1
        return -1 if fresh > 0 else time 
            