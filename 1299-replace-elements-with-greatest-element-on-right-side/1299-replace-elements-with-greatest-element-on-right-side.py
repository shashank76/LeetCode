class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        if n == 1:
            arr = [-1]
        i = n - 1
        temp = -inf
        maxVal = inf
        while i >= 0:
            if i == n-1:
                maxVal = temp = arr[i]
                arr[i] = -1  
            elif maxVal > arr[i]:
                arr[i] = temp
            elif maxVal < arr[i]:
                maxVal = arr[i]
                arr[i] = temp
                temp = maxVal
            i -= 1
        return arr