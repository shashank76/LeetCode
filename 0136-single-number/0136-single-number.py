class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        out = 0
        for i in nums:
            out = out ^ i
        return out
        