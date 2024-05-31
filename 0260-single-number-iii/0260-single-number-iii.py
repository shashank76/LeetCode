class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = 0
        for i in nums:
            xor ^= i

        bit_diff = 1
        while not (xor & bit_diff):
            bit_diff = bit_diff << 1
        
        a, b = 0, 0
        
        for i in nums:
            if bit_diff & i:
                a = a ^ i
            else:
                b = b ^ i
        return [a, b]
            
        