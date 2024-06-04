class Solution:
    def longestPalindrome(self, s: str) -> int:
        counter = Counter(s)
        out = 0
        for i in counter.values():
            out += int(i/2)*2
            if out % 2 == 0 and i%2 == 1:
                out += 1
        return out
            
        