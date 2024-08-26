class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        curMin, curMax = 0, 0
        minSum, maxSum = nums[0], nums[0]
        total = 0
        for i in nums:
            curMin = min(curMin+i, i)
            curMax = max(curMax+i, i)
            total+=i
            minSum = min(minSum, curMin)
            maxSum = max(maxSum, curMax)
        return max(maxSum, total - minSum) if maxSum > 0 else maxSum
        