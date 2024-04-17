class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        out = [0] * len(temperatures)
        stack =[]
        for i, val in enumerate(temperatures):
            while stack and val > stack[-1][1]:
                stkidx, stkval = stack.pop()
                out[stkidx] = i - stkidx
            stack.append([i, val])
        return out
            