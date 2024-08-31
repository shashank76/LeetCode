class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        adjList = defaultdict(list)
        for i in range(len(edges)):
            a, b = edges[i]
            adjList[a].append((b, succProb[i]))
            adjList[b].append((a, succProb[i]))
        
        q = [(-1, start_node)]
        visited = set()
        while len(q):
            val, node = heapq.heappop(q)
            if node in visited:
                continue
            if node == end_node:
                return -val
            visited.add(node)
            for i, prob in adjList[node]:
                heapq.heappush(q, (val*prob, i))
        return 0
        