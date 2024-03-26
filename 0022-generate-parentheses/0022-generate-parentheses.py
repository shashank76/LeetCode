class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        out = []        
        def backtracking(openN, closeN, count):
            count +=1
            if openN == closeN == n:
                out.append("".join(stack))
                return
            
            if openN < n:
                stack.append('(')
                backtracking(openN+1, closeN,count)
                stack.pop()
                
            if closeN < openN:
                stack.append(')')
                backtracking(openN, closeN+1, count)
                stack.pop()
        
        backtracking(0, 0, 0) 
        return out
        