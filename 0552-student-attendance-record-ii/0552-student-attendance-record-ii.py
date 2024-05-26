class Solution:
    def checkRecord(self, n: int) -> int:
        @cache
        
        def helper(i, j, k):
            if i >= n:
                return 1
            out = 0
            if j == 0:
                out += helper(i + 1, j + 1, 0)
            if k < 2:
                out += helper(i + 1, j, k + 1)
            out += helper(i + 1, j, 0)
            return out % mod

        mod = 10**9 + 7
        out = helper(0, 0, 0)
        helper.cache_clear()
        return out
        