class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i == "+":
                stack.append(stack.pop() + stack.pop())
            elif i == "-":
                m = stack.pop()
                n = stack.pop()
                stack.append(n - m)
            elif i == "*":
                stack.append(stack.pop() * stack.pop())
            elif i == "/":
                m = stack.pop()
                n = stack.pop()
                stack.append(int(n / m))
            else:
                stack.append(int(i))
        return stack[0]
        