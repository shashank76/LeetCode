class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        count=0
        out=0
        for i in range(len(nums)):
            if i >=k and nums[i-k] > 1:
                nums[i-k]-= 2
                count-=1
            if count & 1 ^ nums[i]==0:
                if i+k > len(nums):
                    return -1
                nums[i]+=2
                count+=1
                out+=1
        return out
        