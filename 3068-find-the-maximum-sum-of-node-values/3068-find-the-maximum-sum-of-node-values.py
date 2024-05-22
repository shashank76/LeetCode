class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        xor_nums = [(i^k)-i for i in nums]
        xor_nums.sort(reverse=True)
        out = sum(nums)

        for i in range(0, len(nums), 2):
            if i < len(nums)-1: 
                val = xor_nums[i] +  xor_nums[i+1]
                if val > 0: 
                    out += val
        return out
