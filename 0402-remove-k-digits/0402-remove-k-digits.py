class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        out = []
        for i in num:
            while k > 0 and out and out[-1] > i:
                k-=1
                out.pop()
            out.append(i)
        out = out[:len(out) - k]
        while out and out[0] == '0':
            out.pop(0)
        return ''.join(out) if out else '0'
        