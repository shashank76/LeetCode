class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        out, count = 0, 0    
        l, m, r  = 0, 0, 0
        while r < len(nums):
            if nums[r]%2:
                count+=1
            while count > k:
                if nums[l]%2:
                    count-=1
                l +=1
                m=l
            if count == k:
                while nums[m]%2 == 0:
                    m+=1
                out+= m-l+1
            r+=1
        return out        