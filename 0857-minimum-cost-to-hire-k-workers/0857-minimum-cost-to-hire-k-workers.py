class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        sorted_wage_quality = sorted([(a / b, b) for (a, b) in zip(wage, quality)])
        out = float('inf')
        heap = []
        count = 0
        for avg, q in sorted_wage_quality:
            count += q
            heapq.heappush(heap, -q)
            if len(heap) > k: 
                count += heapq.heappop(heap)
            if len(heap) == k: 
                out = min(out, avg * count)
        return out
        