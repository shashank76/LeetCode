class Solution:
    def maximumSwap(self, num: int) -> int:
        num = list(str(num))
        maxVal, maxInd = "0", -1
        ind1 = ind2 = -1 
        i = len(num)-1
        while i >= 0:
            if num[i] > maxVal:
                maxVal = num[i]
                maxInd = i
            if num[i] < maxVal:
                ind1 = i
                ind2 = maxInd
            i-=1
        num[ind1], num[ind2] = num[ind2], num[ind1]
        return int("".join(num))
        