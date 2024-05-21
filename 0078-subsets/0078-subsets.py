class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        out = [[]]
        for i in nums:
            for j in range(len(out)):
                out.append(out[j]+[i])
        return out
        