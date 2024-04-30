class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        bitcount = 0
        count = [0] * 1024
        count[bitcount] += 1
        out = 0

        for i in word:
            bitcount ^= 1 << ord(i) - ord("a")
            out += count[bitcount]
            for i in range(10):
                out += count[bitcount ^ 1 << i]
            count[bitcount] += 1
        return out