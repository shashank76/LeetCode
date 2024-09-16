class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        if not timePoints:
            return 0
        
        times = []
        
        for i in timePoints:
            temp = list(map(int, i.split(':')))
            times += temp[0]*60 + temp[1],
        
        times.sort()
        times += 24*60 + times[0],
        
        n = len(times)
        minuteDiff = float('inf')
        
        for i in range(n-1):
            diff = times[i + 1] - times[i]
            minuteDiff = min(minuteDiff, diff)
        return minuteDiff
        