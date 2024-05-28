class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr) -1
        maxVal = -1
        while n >= 0:
            temp = max(maxVal, arr[n])
            arr[n] = maxVal
            maxVal = temp
            n -= 1
        return arr