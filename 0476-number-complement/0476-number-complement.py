class Solution:
    def findComplement(self, num: int) -> int:
        out = 0
        i = 0
        while num:
            if(num & 1) == 0:
                out+= (1 << i)
            i+=1
            num>>=1
        return out
        
        