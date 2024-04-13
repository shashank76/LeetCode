class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        m, n = len(matrix), len(matrix[0])
        height = [0]*(n+1)
        out=0
        for r in matrix:
            for i in range(n):
                height[i] = height[i] + 1 if r[i] == '1' else 0
            stack = [-1]
            for i in range(n+1):
                while height[i]<height[stack[-1]]:
                    h = height[stack.pop()]
                    w = i-stack[-1]-1
                    out = max(out, h*w)
                stack.append(i)
        return out 