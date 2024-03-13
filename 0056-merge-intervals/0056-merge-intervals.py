class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda i: i[0])
        out = [intervals[0]]
        for i, j in intervals[1:]:
            if i <= out[-1][1]:
                out[-1][1] = max(out[-1][1], j)
            else:
                out.append([i,j])
        return out
        