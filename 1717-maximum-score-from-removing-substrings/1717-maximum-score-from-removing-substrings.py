class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        def remove_substr(st, val):
            nonlocal s
            out = 0
            stack = []
            for i in s:
                if i == st[1] and stack and stack[-1] == st[0]:
                    stack.pop()
                    out+=val
                else:
                    stack.append(i)
            s= "".join(stack)
            return out
        
        out=0
        if x > y:
            out += remove_substr("ab", x)
            out += remove_substr("ba", y)
        else:
            out += remove_substr("ba", y)
            out += remove_substr("ab", x)
        return out
            
        