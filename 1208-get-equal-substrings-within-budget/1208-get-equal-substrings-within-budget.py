class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        curCost, out = 0, 0
        i = 0
        
        for j in range(len(s)):
            curCost += abs(ord(s[j]) - ord(t[j]))
            
            if maxCost < curCost:
                curCost -= abs(ord(s[i]) - ord(t[i]))
                i+=1
            out = max(out, j-i+1)
        return out 
            
        
        
        