class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows, cols = len(obstacleGrid), len(obstacleGrid[0])
        prevRow = [0] * cols
        prevRow[cols-1] = 1

        for i in range(rows-1, -1, -1):
            for j in range(cols-1, -1, -1):
                if obstacleGrid[i][j] == 1:
                    prevRow[j] = 0
                elif j+1 < cols:
                    prevRow[j] = prevRow[j+1] + prevRow[j]
        return prevRow[0]
        