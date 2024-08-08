class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        count = rows * cols
        r, c = rStart, cStart
        out = []
        walDir = [[0,1], [1,0], [0,-1], [-1,0]]
        i, j = 0, 1
        while count > 0:
            for _ in range(2):
                r1, c1 = walDir[i]
                for x in range(j):
                    if 0 <= r < rows and 0 <= c < cols:
                        out.append([r, c])
                        count-=1
                    r, c = r+r1,c+c1
                i = (i+1)%4
            j+=1  
        return out
            
            
            
            
            
        