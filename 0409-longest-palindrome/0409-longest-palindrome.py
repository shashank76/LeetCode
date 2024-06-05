class Solution:
    def longestPalindrome(self, s: str) -> int:
        visited = set()
        out = 0
        for i in s:
            if i in visited:
                visited.remove(i)
                out += 2
            else:
                visited.add(i)
        if visited:
            out+=1
        return out
            
        