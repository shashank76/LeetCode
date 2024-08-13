class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-i for i in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            s1= heapq.heappop(stones)
            s2= heapq.heappop(stones)
            if s2>s1:
                heapq.heappush(stones, s1-s2)
        if not stones:
            stones.append(0)
            
        return abs(stones[0])
            
        