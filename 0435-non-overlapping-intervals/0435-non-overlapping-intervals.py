class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda i:i[0])
        count = 0
        lastEnd = intervals[0][1]
        for i, j in intervals[1:]:
            if i >= lastEnd:
                lastEnd = j
            else:
                count +=1
                lastEnd = min(lastEnd, j)
        return count
        