class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        out=0
        for i in nums:
            out^=i
            
        out=out^k
        return bin(out).count('1')
        