class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        i = 0
        out = {}
        minHeap = []
        for q in sorted(queries):
            while i < len(intervals) and intervals[i][0] <= q:
                l, r = intervals[i]
                heapq.heappush(minHeap, (r-l+1, r))
                i+=1
            
            while minHeap and minHeap[0][1] < q:
                heapq.heappop(minHeap)
            
            out[q] = minHeap[0][0] if minHeap else -1
            
        return [out[x] for x in queries]
            
        