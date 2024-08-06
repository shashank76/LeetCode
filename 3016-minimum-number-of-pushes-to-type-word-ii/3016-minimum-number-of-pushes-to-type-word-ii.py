class Solution:
    def minimumPushes(self, word: str) -> int:
        count = [0]*26
        out = 0
        
        for i in word:
            count[ord(i) - ord('a')] +=1
        
        count.sort(reverse=True)
        for i, v in enumerate(count):
            out+= v * (1+i//8)
        return out
            
        