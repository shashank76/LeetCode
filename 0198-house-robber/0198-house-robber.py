class Solution:
    def rob(self, nums: List[int]) -> int:
        i=0
        max1, max2 = 0, 0        
        while i < len(nums):
            temp = max(max1 + nums[i], max2)
            max1, max2 = max2, temp
            i+=1
        return max2
            
        