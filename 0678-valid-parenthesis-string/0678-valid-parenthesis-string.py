class Solution:
    def checkValidString(self, s: str) -> bool:
        min_count, max_count = 0, 0
        for i in s:
            if i == "(":
                min_count, max_count = min_count+1, max_count+1
            elif i == ")":
                min_count, max_count = min_count-1, max_count-1
            else:
                min_count, max_count = min_count-1, max_count+1
            if max_count < 0:
                return False
            if min_count < 0:
                min_count = 0
        return min_count == 0
                
        