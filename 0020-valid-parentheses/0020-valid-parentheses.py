class Solution:
    def isValid(self, s: str) -> bool:
        bracs = { ')': '(', '}': '{', ']': '['}
        stack = []
        for i in s:
            if i == '(' or i == '{' or i == '[':
                stack.append(i)
            else: 
                if stack and stack[-1] == bracs[i]:
                    stack.pop()
                else:
                    return False
        return len(stack) == 0
                
        