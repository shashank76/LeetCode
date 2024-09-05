class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        out = float('inf')
        l = 0
        totalSum = 0
        for r in range(len(nums)):
            totalSum += nums[r]
            while totalSum >= target:
                out = min(out, r-l+1)
                totalSum -= nums[l]
                l+=1
        return 0 if out == float('inf') else out
        