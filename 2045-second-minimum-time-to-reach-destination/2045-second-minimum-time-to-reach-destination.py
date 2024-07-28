class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        dictVals = defaultdict(list)
        for i, j in edges:
            dictVals[i].append(j)
            dictVals[j].append(i)
            
        q = deque([1])
        cur, out = 0, -1
        visited = defaultdict(list)
        
        while q:
            for i in range(len(q)):
                node = q.popleft()
                if node == n: 
                    if out != -1:
                        return cur
                    out = cur
                    
                for j in dictVals[node]:
                    dist = visited[j]
                    if len(dist) == 0 or (len(dist) == 1 and dist[0] != cur):
                        q.append(j)
                        dist.append(cur)
            if (cur // change)%2 == 1:
                cur += change - (cur%change)
            cur += time
            
                        
                    
                
                    
                
        