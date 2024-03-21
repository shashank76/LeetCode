class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}
        
        def findExpression(i, count):
            if i == len(nums):
                return 1 if count == target else 0
            if (i, count) in dp:
                return dp[(i, count)]
            dp[(i, count)] = (findExpression(i+1, count+nums[i]) + 
                              findExpression(i+1, count-nums[i]))
            return dp[(i, count)]
        return findExpression(0,0)
        