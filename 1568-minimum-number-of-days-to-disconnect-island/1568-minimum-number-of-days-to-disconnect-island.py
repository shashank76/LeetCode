class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        R = len(grid)
        C = len(grid[0])
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        def dfs(r, c, visit):
            if r < 0 or c < 0 or c >= C or r >= R or (r, c) in visit or grid[r][c] == 0:
                return
            visit.add((r, c))
            for dr, dc in directions:
                dfs(r + dr, c + dc, visit)

        def count_islands():
            islands = 0
            visited = set()
            for r in range(R):
                for c in range(C):
                    if grid[r][c] == 1 and (r, c) not in visited:
                        islands += 1
                        dfs(r, c, visited)
            return islands

        islands = count_islands()
        if islands != 1:
            return 0

        for r in range(R):
            for c in range(C):
                if grid[r][c] == 1:
                    grid[r][c] = 0
                    islands = count_islands()
                    if islands != 1:
                        return 1
                    grid[r][c] = 1
        return 2
        