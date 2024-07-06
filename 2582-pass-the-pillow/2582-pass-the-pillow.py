class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        numPass = time // (n-1)
        if numPass % 2 == 0:
            return 1 + time % (n-1)
        else:
            return n - time % (n-1)
            
            
        