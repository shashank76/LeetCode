class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        pairVals = []
        for i, v in enumerate(nums):
            val = str(v)
            mappedVal =0
            for j in val:
                mappedVal *= 10
                mappedVal += mapping[int(j)]
            pairVals.append((mappedVal, i))
        
        pairVals.sort()
        return [nums[x[1]] for x in pairVals]