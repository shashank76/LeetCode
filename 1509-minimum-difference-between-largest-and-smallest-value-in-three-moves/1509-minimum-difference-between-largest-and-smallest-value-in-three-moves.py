class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 4:
            return 0
        minVals = sorted(heapq.nsmallest(4, nums))
        maxVals = sorted(heapq.nlargest(4, nums))
        i = 0
        out = float('inf')
        while i < 4:
            out = min(out, maxVals[i] - minVals[i]) 
            i+=1
        return out
        