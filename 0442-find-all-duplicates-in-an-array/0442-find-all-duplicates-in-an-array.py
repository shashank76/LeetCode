class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        out = []
        for i in range(len(nums)):
            val = abs(nums[i])
            if nums[val-1] < 0:
                out.append(val)
            nums[val-1] = -nums[val-1]
        return out
        