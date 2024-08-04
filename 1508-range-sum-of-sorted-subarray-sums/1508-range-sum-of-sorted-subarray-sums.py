class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        out = []
        mod = 10**9+7
        i =0
        while i <len(nums):
            out.append(nums[i])
            for j in range(i+1, len(nums)):
                out.append((out[-1] + nums[j]))
            i+=1
        out.sort()
        res = 0
        for x in range(left-1, right):
            res+=out[x]
        return res %mod       