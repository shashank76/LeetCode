class Solution:
    def specialArray(self, nums: List[int]) -> int:
        counter = [0] * (len(nums) + 1)
        
        for i in nums:
            i = i if i < len(nums) else len(nums)
            counter[i] += 1
        
        out = 0
        i = len(nums)
        while i >= 0:
            out += counter[i]
            if i == out:
                return out
            i-=1
        return -1
        
        # nums.sort()
        # n = len(nums)
        # prev = 0
        # i = 0
        # while i < len(nums):
        #     if nums[i] < n:
        #         n-=1
        #     elif nums[i] >= n and prev < n:
        #         return n
        #     prev = nums[i]
        #     i+=1
        # return -1
        