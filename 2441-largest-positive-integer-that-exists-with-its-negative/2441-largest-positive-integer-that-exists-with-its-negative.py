class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        out = 0
        for i in nums:
            val = max(out, i)
            if (-1 * val) in nums:
                out = val
        return out if out > 0 else -1
            
        