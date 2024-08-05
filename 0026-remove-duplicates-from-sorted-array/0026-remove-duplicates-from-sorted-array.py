class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = 0
        for i in range(1, len(nums)):
            if nums[i-1] == nums[i]:
                count+=1
            else:
                nums[i-count] = nums[i]
        return len(nums) - count
                
        