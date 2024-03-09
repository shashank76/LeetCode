class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        out = 0
        vals = Counter(nums).values()
        for i in vals:
            if i == max(vals):
                out+=i
        return out
        