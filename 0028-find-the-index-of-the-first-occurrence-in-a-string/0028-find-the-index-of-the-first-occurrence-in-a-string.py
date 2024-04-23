class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        i = 0
        while i < len(haystack):
            j = 0
            out = i
            while j < len(needle) and i < len(haystack) and haystack[i] == needle[j]:
                i += 1
                j += 1
            if j == len(needle):
                return out
            i = out+1
        return -1
                    
                
                
        
        