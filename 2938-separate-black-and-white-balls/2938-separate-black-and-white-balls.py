class Solution:
    def minimumSteps(self, s: str) -> int:
        out = 0
        blacks = 0

        for i in s:
            if i == '1':
                blacks += 1
            else:
                out += blacks
        
        return out
        