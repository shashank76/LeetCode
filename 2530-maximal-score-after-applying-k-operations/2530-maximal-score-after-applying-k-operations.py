class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        heap = []
        out = 0
        for i in nums:
            heapq.heappush(heap, -i)
            
        for _ in range(k):
            x = -1*heapq.heappop(heap)
            out += x
            i=(x+2)//3
            heapq.heappush(heap, -i)
            
        return out
                
        