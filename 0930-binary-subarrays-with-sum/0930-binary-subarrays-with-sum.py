class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:

        def helper(x):
            l = r = 0
            out = 0
            if x<0:
                return 0
            
            for i in range(len(nums)):
                r += nums[i]
                while r > x:
                    r-= nums[l]
                    l+=1
                out += (i-l+1)
            return out
        
        return helper(goal) - helper(goal-1)