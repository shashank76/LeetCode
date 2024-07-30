class Solution:
    def minimumDeletions(self, s: str) -> int:
        a_counter = 0
        for i in range(len(s)):
            if s[i] =='a':
                a_counter+=1
        
        b_counter, out = 0, len(s)-1
        for i, v in enumerate(s):
            if v == 'a':
                a_counter-=1
            out = min(out, b_counter+a_counter)
            if v == 'b':
                b_counter+=1
        return out
            
            
        