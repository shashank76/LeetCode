class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points = sorted(points)
        out = 1
        x, y = points[0]
        for m, n in points:
            if (x >= m and x <= n) or (x <= m and y >= m):
                x = max(m, x)
                y = min(n, y)
                continue
            x, y = m, n
            out += 1
        return out