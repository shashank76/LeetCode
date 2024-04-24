class Solution:
    def tribonacci(self, n: int) -> int:
        T0 = 0
        T1 = T2 = 1
        trib_ser = [0, 1, 1]
        if n < 3:
            return trib_ser[n]
        
        for _ in range(3, n+1):
            out = T0 + T1 + T2
            T0 = T1
            T1 = T2
            T2 = out
        return out

