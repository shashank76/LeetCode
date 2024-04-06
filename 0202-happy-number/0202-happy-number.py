class Solution:
    def isHappy(self, n: int) -> bool:
        hashVal = set()
        while n not in hashVal:
            hashVal.add(n)
            n = self.calSqr(n)
            if n == 1:
                return True
        return False
    
    def calSqr(self, n):
        out = 0
        while n:
            x = n % 10
            x = x**2 
            out += x
            n = n // 10
        return out

        
            
        