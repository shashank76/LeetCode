class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        out = start ^ goal
        count = 0

        while out > 0:
            if out & 1 == 1:
                count += 1
            out >>= 1
        
        return count
        