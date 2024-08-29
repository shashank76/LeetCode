class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        n = len(stones)
        visited = [False] * n
        groups = 0
        
        def dfs(ind):
            visited[ind] = True

            for i in range(n):
                if (not visited[i]) and (stones[ind][0] == stones[i][0] or 
                     stones[ind][1] == stones[i][1]):
                    dfs(i) 

        for i in range(n):
            if not visited[i]:
                dfs(i)
                groups += 1
        
        return n - groups