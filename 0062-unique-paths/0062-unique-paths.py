class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        prevRow = [0] * n

        for i in range(m-1, -1, -1):
            curRow = [0] * n
            curRow[n-1] = 1
            for j in range(n-2, -1, -1):
                if curRow[j] == 0:
                    curRow[j] = curRow[j+1] + prevRow[j]
                else:
                    continue
            prevRow = curRow  
        return prevRow[0]
        