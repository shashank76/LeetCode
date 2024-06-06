class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False
        
        maps = Counter(hand)
        minHeap = list(maps.keys())
        heapq.heapify(minHeap)

        while minHeap:
            val = minHeap[0]
            for num in range(val, val + groupSize):
                if num not in maps:
                    return False
                maps[num] -= 1
                if maps[num] == 0:
                    del maps[num]
                    heapq.heappop(minHeap)
        return True
        