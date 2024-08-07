class Solution:
    def climbStairs(self, n: int) -> int:
        i = j = 1
        
        for x in range(n-1):
            temp = j
            j = i+j
            i = temp
        return j
        