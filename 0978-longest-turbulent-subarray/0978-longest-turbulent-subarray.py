class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        l, r = 0, 1
        out, preVal = 1, ''
        while r < len(arr):
            if (arr[r-1] > arr[r]) and (preVal != '>'):
                out=max(out, r-l+1)
                preVal='>'
                r+=1
            elif (arr[r-1] < arr[r]) and (preVal != '<'):
                out=max(out, r-l+1)
                preVal='<'
                r+=1
            else:
                if arr[r-1] == arr[r]:
                    r=r+1
                l=r-1
                preVal=''
        return out
                
                
                
        