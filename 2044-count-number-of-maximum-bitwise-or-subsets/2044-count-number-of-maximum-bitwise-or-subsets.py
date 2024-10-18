class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        target = 0
        for num in nums:
            target |= num

        n = len(nums)
        N = 2**n

        out = 0
        for i in range(1,N):
            curr_val = 0
            for j in range(n):
                if i&(1<<j):
                    curr_val |= nums[j]
            if curr_val == target:
                out+=1
        return out
        