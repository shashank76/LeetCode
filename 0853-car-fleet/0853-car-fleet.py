class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        paired = []
        i = 0
        while i < len(position):
            paired.append([position[i], speed[i]])
            i+=1
        
        stack = []
        
        for p, s in sorted(paired)[::-1]:
            stack.append((target-p)/s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)
        