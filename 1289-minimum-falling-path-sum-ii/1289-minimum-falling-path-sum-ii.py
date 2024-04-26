class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        
        def getMinTwo(row):
            minVals = []
            for i, v in row:
                if len(minVals) < 2:
                    minVals.append((i, v))
                elif minVals[1][1] > v:
                    minVals.pop()
                    minVals.append((i, v))
                minVals.sort(key= lambda x: x[1])
            return minVals
            
            
        n = len(grid)
        firstRow = [(i, v) for i, v in enumerate(grid[0])] 
        dp = getMinTwo(firstRow)
        for i in range(1, n):
            nxt_dp = []
            for p in range(n):
                curVal = grid[i][p]
                minVal = float("inf")
                for idx, val in dp:
                    if p != idx:
                        minVal = min(minVal,  curVal + val) 
                nxt_dp.append((p, minVal))
                nxt_dp = getMinTwo(nxt_dp)
            dp = nxt_dp
        return min([val for i, val in dp])
        