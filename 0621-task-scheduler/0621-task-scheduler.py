class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = Counter(tasks)
        maxHeap = [-i for i in counter.values()]
        heapq.heapify(maxHeap)
        out = 0
        q=deque()
        while maxHeap or q:
            out += 1
            if maxHeap:
                cnt = 1+ heapq.heappop(maxHeap)
                if cnt:
                    q.append([cnt, out+n])
            if q and q[0][1] == out:
                heapq.heappush(maxHeap, q.popleft()[0])
        return out
                
            
            
            
        