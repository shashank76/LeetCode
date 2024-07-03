class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 4:
            return 0
        minVal = float('inf')
        nums.sort()
        for i in range(4):
            r = len(nums)-4+i
            minVal = min(minVal, nums[r] - nums[i]) 
        return minVal
        