class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        out = 0
        count, max_val = 0, max(nums)
        i = 0
        for j in range(len(nums)):
            if nums[j] == max_val:
                count +=1
            while count > k or ( i <=j and count == k and nums[i] != max_val):
                if nums[i] == max_val:
                    count -=1
                i+=1
                
            if count == k:
                out += i+1
            
        return out
        
                
        