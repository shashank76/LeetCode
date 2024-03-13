class Solution:
    def pivotInteger(self, n: int) -> int:
        leftSum, rightSum = 0, sum(range(1, n + 1))
        for i in range(1, n+1):
            leftSum += i 
            if leftSum == rightSum:
                return i
            rightSum -= i
        return -1
            
            
        