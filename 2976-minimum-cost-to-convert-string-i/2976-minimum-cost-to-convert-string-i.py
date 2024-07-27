class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        dictVal = defaultdict(list)
        i = 0
        while i < len(original):
            dictVal[original[i]].append((changed[i], cost[i]))
            i+=1
        
        def findMinCost(x):
            min_cost = {}
            heap = [(0, x)]
            while heap:
                val, node = heapq.heappop(heap)
                if node in min_cost:
                    continue
                min_cost[node] = val
                for nei, cost in dictVal[node]:
                    total_dist = val+cost
                    heapq.heappush(heap, (total_dist, nei)) 
            return min_cost
        
        minCost = {}
        for c in set(source):
            minCost[c] = findMinCost(c)
        
        out, i = 0, 0
        while i < len(source):
            if target[i] not in minCost[source[i]]:
                return -1
            out+= minCost[source[i]][target[i]]
            i+=1
        return out
        