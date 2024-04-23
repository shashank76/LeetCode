class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxVal = 0
        stack = []
        
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                idx, val = stack.pop()
                maxVal = max(maxVal, val * (i-idx))
                start = idx
            stack.append([start, h])
        
        
        for i, h in stack:
            maxVal = max(maxVal, h * (len(heights) - i))
        return maxVal
            
            
                
        