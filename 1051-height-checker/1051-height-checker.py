class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = sorted(heights)
        i = 0
        out = 0
        while i < len(heights):
            if expected[i] != heights[i]:
                out += 1
            i+=1
        return out