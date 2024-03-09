class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        out = float('inf')
        i, j = 0, k-1
        nums.sort()
        while j < len(nums):
            out = min(out, nums[j]-nums[i])
            i+=1
            j+=1
        return out
        