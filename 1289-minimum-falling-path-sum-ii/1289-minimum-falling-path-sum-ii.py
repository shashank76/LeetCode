class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dp = grid[0]
        
        for i in range(1, n):
            x = float("inf")
            nxt_dp = [x] * n
            for p in range(n):
                for q in range(n):
                    if p != q:
                        nxt_dp[p] = min(nxt_dp[p], grid[i][p]+dp[q]) 
            dp = nxt_dp
        return min(dp)
        