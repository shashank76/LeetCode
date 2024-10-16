class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        out = ''
        maxHeap = []
        for cnt, val in [(-a, 'a'), (-b, 'b'), (-c, 'c')]:
            if cnt != 0:
                heapq.heappush(maxHeap, (cnt, val))
        
        while maxHeap:
            cnt, val = heapq.heappop(maxHeap)
            if len(out) > 1 and (out[-1] == out[-2] == val):
                if not maxHeap:
                    break
                cnt1, val1 = heapq.heappop(maxHeap)
                out+=val1
                cnt1+=1
                if cnt1:
                    heapq.heappush(maxHeap, (cnt1, val1))
            else:
                out+=val
                cnt+=1
            if cnt:
                heapq.heappush(maxHeap, (cnt, val))
            
        return out