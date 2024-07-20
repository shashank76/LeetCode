class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        out = [[0]*len(colSum) for _ in range(len(rowSum))]
        for i in range(len(rowSum)):
            out[i][0] = rowSum[i]
            
        for i in range(len(colSum)):
            sumVal = 0
            for j in range(len(rowSum)):
                sumVal+=out[j][i]
            
            x = 0
            while sumVal > colSum[i]:
                diff = sumVal - colSum[i]
                diffVal = min(out[x][i], diff)
                out[x][i] -= diffVal
                out[x][i+1] += diffVal
                sumVal -= diffVal
                x+=1
        return out
        