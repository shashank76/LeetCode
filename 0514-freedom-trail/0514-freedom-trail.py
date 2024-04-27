class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        cache = {}
        
        def findMinTrail(k, v):
            if v == len(key):
                return 0
            if (k, v) in cache:
                return cache[(k, v)]
            
            out = float('inf')
            for i, val in enumerate(ring):
                if val == key[v]:
                    minDist = min(abs(k-i), len(ring) - abs(k-i))
                    out = min(out, minDist+1+findMinTrail(i, v+1))
            cache[(k, v)] = out
            return out
        
        return findMinTrail(0, 0)
                
                    
            
        