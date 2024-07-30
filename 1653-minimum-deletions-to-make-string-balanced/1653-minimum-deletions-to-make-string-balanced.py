class Solution:
    def minimumDeletions(self, s: str) -> int:
        a_counter = b_counter = 0
        out = len(s)
        for i in s:
            if i =='a':
                a_counter+=1
    
        for i, v in enumerate(s):
            if v == 'a':
                a_counter-=1
            out = min(out, b_counter+a_counter)
            if v == 'b':
                b_counter+=1
        return out
            
            
        