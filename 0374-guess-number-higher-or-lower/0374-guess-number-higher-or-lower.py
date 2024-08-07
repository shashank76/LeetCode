# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        i = 0
        while i <= n:
            num = (i + n) // 2
            if guess(num) > 0:
                i = num +1
            elif guess(num) < 0:
                n = num -1
            else:
                return num
                
        