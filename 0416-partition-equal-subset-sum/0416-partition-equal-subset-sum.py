class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if len(nums) < 2 or sum(nums) % 2:
            return False
        target = sum(nums)//2
        dp = set()
        dp.add(0)
        for i in nums:
            new_dp = dp.copy()
            for j in dp:
                new_dp.add(i+j)
            dp = new_dp
        return True if target in dp else False
        