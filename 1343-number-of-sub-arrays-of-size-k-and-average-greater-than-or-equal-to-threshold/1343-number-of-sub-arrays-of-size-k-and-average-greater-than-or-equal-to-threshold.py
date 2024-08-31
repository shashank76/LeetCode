class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        count = 0
        i = 0
        totalSum = sum(arr[:k-1])
        while i < len(arr)-k+1:
            totalSum += arr[i+k-1]
            if (totalSum/k) >= threshold:
                count+=1
            totalSum-=arr[i]
            i+=1
        return count
                
        