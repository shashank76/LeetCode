class Solution:
    def maxArea(self, height: List[int]) -> int:
        out = 0
        l, r = 0, len(height) - 1

        while l < r:
            area = (r-l) * min(height[l], height[r])
            out = max(out, area)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return out