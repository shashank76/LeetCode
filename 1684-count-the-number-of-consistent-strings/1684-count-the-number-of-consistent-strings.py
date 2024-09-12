class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count = 0
        
        for s in words:
            for i in range(len(s)):
                if s[i] not in allowed:
                    break 
                if i == len(s)-1:
                    count+=1     
        return count
        