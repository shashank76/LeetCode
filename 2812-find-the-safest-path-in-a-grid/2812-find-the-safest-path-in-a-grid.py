class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n = len(grid)
        
        def isValidIndex(r, c):
            return min(r, c) >= 0 and max(r,c) < n
        
        def calculateDist():
            q = collections.deque()
            min_dist={}
            
            for i in range(n):
                for j in range(n):
                    if grid[i][j]:
                        q.append([i,j,0])
                        min_dist[i, j] = 0           
            while q:
                i, j, dist = q.popleft()
                adj_vals = [[i+1, j], [i-1, j], [i, j+1], [i, j-1]]
                for x, y in adj_vals:
                    if isValidIndex(x, y) and (x, y) not in min_dist:
                        min_dist[x, y] = dist+1
                        q.append([x, y, dist+1])
            return min_dist
        
        min_dist = calculateDist()
        maxHeap = [(-min_dist[(0,0)], 0, 0)]
        visited = set()
        visited.add((0,0))
        while maxHeap:
            dist, r, c = heapq.heappop(maxHeap)
            dist = -dist
            if (r, c) == (n-1,n-1):
                return dist

            adj_vals = [[r+1, c], [r-1, c], [r, c+1], [r, c-1]]
            for x, y in adj_vals:
                if isValidIndex(x, y) and (x, y) not in visited:
                    visited.add((x, y))
                    new_dist = min(dist, min_dist[x, y])
                    heapq.heappush(maxHeap, (-new_dist, x, y))