class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        m = len(rolls)
        totalVal = mean *(m+n)
        missingVal = totalVal - sum(rolls)
        out = []
        
        if missingVal > 6*n or missingVal < n:
            return out
        
        
        while n:
            val = min(6, missingVal-n+1)
            out.append(val)
            missingVal-=val
            n-=1
           
        return out
        