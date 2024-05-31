class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        out = []
        
        for i in nums:
            if i in out:
                out.remove(i)
            else:
                out.append(i)
        return out
            
        