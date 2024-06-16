class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        out = 0
        i = 0
        maxLen = 0
        while maxLen < n:
            if i < len(nums) and nums[i] <= maxLen + 1:
                maxLen += nums[i]
                i+=1
            else:
                out += 1
                maxLen += maxLen + 1
        return out 
        