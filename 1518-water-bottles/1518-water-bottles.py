class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        out = 0
        empty = 0
        while numBottles > 0:
            out+=numBottles
            empty+=numBottles
            numBottles = empty // numExchange
            empty = empty % numExchange
        return out
        