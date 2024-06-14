class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int: 
        nums.sort()
        count = 0
        i = 1
        while i < len(nums):
            if nums[i-1] >= nums[i]:
                val = nums[i-1] - nums[i] + 1
                nums[i] += val
                count +=val
            i+=1
        return count
        