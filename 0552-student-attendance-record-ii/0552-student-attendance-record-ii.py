class Solution:
    def checkRecord(self, n: int) -> int:
        mod = 10**9 + 7
        if n == 1:
            return 3
        
        temp = { (0,0): 1, (0,1): 1, (0,2): 0, (1,0): 1, (1,1): 0, (1,2): 0 }
        for i in range(n-1):
            out = defaultdict(int)
            
            out[(0,0)] = ((temp[(0,0)] + temp[(0,1)]) % mod + temp[(0,2)]) % mod
            out[(1,0)] = ((temp[(1,0)] + temp[(1,1)]) % mod + temp[(1,2)]) % mod
            
            out[(0,1)] = temp[(0,0)]
            out[(1,1)] = temp[(1,0)]
            out[(0,2)] = temp[(0,1)]
            out[(1,2)] = temp[(1,1)]
            
            out[(1,0)] = (out[(1,0)] + ((temp[(0,0)] + temp[(0,1)]) % mod + temp[(0,2)]) % mod) % mod
            
            temp = out
            
        return sum(temp.values()) % mod
            
        