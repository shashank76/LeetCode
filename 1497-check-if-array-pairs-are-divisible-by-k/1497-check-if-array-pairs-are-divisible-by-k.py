class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        pairRem = [0] * k
        for i in arr:
            rem = i % k
            pairRem[rem] += 1
        if pairRem[0] % 2 != 0:
            return False
        i = 1
        while i < k:
            if pairRem[i] != pairRem[k-i]:
                return False
            i+=1
        return True
    
        
        
        