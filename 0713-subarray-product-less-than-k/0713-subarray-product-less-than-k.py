class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        l = out = 0
        prod = 1
        for r in range(len(nums)):
            prod *= nums[r]
            
            while l<=r and prod >= k:
                prod = prod // nums[l]
                l+=1
            out += r-l+1
        return out
        