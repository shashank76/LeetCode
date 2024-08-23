class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        dp = {}
        def dfs(isAlice, i, M):
            if i == len(piles):
                return 0
            
            if (isAlice, i, M) in dp:
                return dp[(isAlice, i, M)]
            
            out = 0 if isAlice else float('inf')
            totalVal = 0
            for X in range(1, 2*M+1):
                if i+X > len(piles):
                    break
                totalVal+= piles[i+X-1]
                if isAlice:
                    out = max(out, totalVal+dfs(not isAlice, i+X, max(M,X))) 
                else:
                    out = min(out, dfs(not isAlice, i+X, max(M,X)))
                
            dp[(isAlice, i, M)] = out
            return out
        
        return dfs(True, 0, 1)
            
        