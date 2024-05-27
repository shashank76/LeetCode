class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        prev = 0
        i = 0
        while i < len(nums):
            if nums[i] < n:
                n-=1
            elif nums[i] >= n and prev < n:
                return n
            prev = nums[i]
            i+=1
        return -1
        