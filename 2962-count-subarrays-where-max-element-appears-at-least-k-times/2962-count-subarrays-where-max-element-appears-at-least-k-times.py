class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        out = 0
        count, max_val = 0, max(nums)
        l = 0
        for r in range(len(nums)):
            if nums[r] == max_val:
                count +=1
            while count > k or ( l <= r and count == k and nums[l] != max_val):
                if nums[l] == max_val:
                    count -=1
                l+=1
                
            if count == k:
                out += l+1
            
        return out
        
                
        