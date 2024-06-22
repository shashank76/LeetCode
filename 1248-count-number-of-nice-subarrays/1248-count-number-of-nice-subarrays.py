class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        # out = 0
        # i = 0
        # while i < len(nums):
        #     count = 0
        #     for j in range(i, len(nums)):
        #         if nums[j] %2 != 0:
        #             count+=1
        #         if count == k:
        #             out+=1
        #             continue
        #     i+=1
        # return out
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