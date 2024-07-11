class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        for i in s:
            if i == ")":
                substr = []
                while stack[-1] != "(":
                    substr.append(stack.pop())
                stack.pop()
                stack.extend(substr)
            else:
                stack.append(i)
                
        return "".join(stack)
        