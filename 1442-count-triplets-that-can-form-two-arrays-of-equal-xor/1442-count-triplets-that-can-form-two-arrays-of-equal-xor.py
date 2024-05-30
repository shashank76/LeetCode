class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        n = len(arr) - 1
        out = 0
        
        for i in range(n):
            a = 0
            for j in range(i+1, n+1):
                a ^= arr[j-1]
                b = 0
                for k in range(j, n+1):
                    b ^= arr[k]
                    if a == b:
                        out+=1
        return out
        
        