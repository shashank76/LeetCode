class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        dictVals = defaultdict(list)
        for n1, n2, dist in edges:
            dictVals[n1].append((n2, dist))
            dictVals[n2].append((n1, dist))
            
        def find_smallest(i):
            visited = set()
            heap = [(0, i)]
            while heap:
                dist1, node = heapq.heappop(heap)
                if node in visited:
                    continue
                visited.add(node)
                for x, dist2 in dictVals[node]:
                    total_dist = dist1 + dist2
                    if total_dist <= distanceThreshold:
                        heapq.heappush(heap, (total_dist, x))
            return len(visited) -1
                    
        
        out, minVal = -1, n+1
        for i in range(n):
            count = find_smallest(i)
            if count <= minVal:
                out, minVal = i, count
        return out
            
        