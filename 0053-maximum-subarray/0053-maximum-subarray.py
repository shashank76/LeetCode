class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curSum, maxSum = 0, nums[0]
        for i in nums:
            curSum = max(curSum, 0)
            curSum+=i
            maxSum = max(curSum, maxSum)
        return maxSum
        