class Solution:
    def scoreOfString(self, s: str) -> int:
        out = 0
        for i in range(1, len(s)):
            out+= abs(ord(s[i]) - ord(s[i-1]))
        return out