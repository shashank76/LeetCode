class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digitDict = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        out = []
        
        def backtracking(i, cur):
            if len(digits) == len(cur):
                out.append(cur)
                return
            
            for x in digitDict[digits[i]]:
                backtracking(i+1, cur+x)
        
        if digits:
            backtracking(0, "")
        return out
        
        