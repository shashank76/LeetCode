class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        dictVals = {0: -1}
        count = 0
        
        for i, v in enumerate(nums):
            count += v
            val = count % k
            if val not in dictVals:
                dictVals[val] = i
            elif i - dictVals[val] > 1:
                return True
        return False
        