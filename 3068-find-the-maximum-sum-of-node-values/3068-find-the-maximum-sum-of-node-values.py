class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        count = 0
        minVal = float('inf')
        out = 0

        for i in nums:
            val = i ^ k
            if i < val:
                count += 1
                out += val
                minVal = min(minVal, val - i)
            else:
                out += i
                minVal = min(minVal, i - val)

        if count % 2:
            out -= minVal

        return out
