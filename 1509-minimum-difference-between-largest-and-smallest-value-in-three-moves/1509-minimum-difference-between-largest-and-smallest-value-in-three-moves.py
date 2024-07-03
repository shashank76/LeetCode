class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 4:
            return 0
        minVal = float('inf')
        nums.sort()
        for i in range(4):
            j = len(nums)-4+i
            print(nums, i, j)
            minVal = min(minVal, nums[j] - nums[i]) 
        return minVal
        