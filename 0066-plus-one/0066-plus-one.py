class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)-1
        carry = 1
        while carry:
            if digits[n] < 9:
                digits[n]+=1
                carry-=1
            elif digits[n] == 9:
                if n == 0:
                    digits[n] = 1
                    digits.append(0)
                    carry-=1
                else:
                    digits[n] = 0
            n-=1
        return digits
            
        