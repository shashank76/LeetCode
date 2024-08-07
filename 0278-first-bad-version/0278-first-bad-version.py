# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        out  = n
        i = 0
        while i <= n:
            ver = (i+n) // 2
            if isBadVersion(ver):
                out = min(out, ver)
                n = ver -1
            else:
                i = ver +1
        return out
                
        