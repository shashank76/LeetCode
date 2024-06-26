class Solution:
    def maxDepth(self, s: str) -> int:
        count = 0
        out = 0
        for i in s:
            if i == "(":
                count+=1
            elif i == ")":
                count-=1
            out = max(out, count)
        return out
        