class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m = len(s1)
        n = len(s2)
        s1_counter = Counter(s1)
        
        for i in range(n-m+1):
            s2_counter = Counter(s2[i:i+m])
            if s2_counter == s1_counter:
                return True
            
        return False
        