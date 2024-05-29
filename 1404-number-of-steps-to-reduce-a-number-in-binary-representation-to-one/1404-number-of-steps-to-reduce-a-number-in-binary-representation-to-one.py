class Solution:
    def numSteps(self, s: str) -> int:
        count = 0
        s = int(s,2)
        while s != 1:
            if s % 2 == 0:
                s = s // 2
            else:
                s += 1
            count+=1
        return count
        