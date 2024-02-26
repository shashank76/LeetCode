class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_vals = {}
        for i, x in enumerate(nums):
            diff = target - x
            if diff in hash_vals:
                return [i, hash_vals[diff]]
            hash_vals[x] = i