class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = set()
        posDir = set()
        negDir = set()
        out = []
        grid = [['.']*n for _ in range(n)]
        
        def backtracking(r):
            if r == n:
                curr = ["".join(row) for row in grid]
                out.append(curr)
                return 
            
            for c in range(n):
                if c in cols or (r+c) in posDir or (r-c) in negDir:
                    continue
                
                cols.add(c)
                posDir.add(r+c)
                negDir.add(r-c)
                grid[r][c] = 'Q'
                
                backtracking(r+1)
                
                cols.remove(c)
                posDir.remove(r+c)
                negDir.remove(r-c)
                grid[r][c] = '.'
                
        backtracking(0)
        return out
        
        