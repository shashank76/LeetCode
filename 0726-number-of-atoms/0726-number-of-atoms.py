class Solution:
    def countOfAtoms(self, formula: str) -> str:
        n = len(formula)
        stack = [Counter()]
        i = 0

        while i<n:
            c = formula[i]

            if c == '(':
                stack.append(Counter())
                i+=1
            elif c == ')':
                curr_counter = stack.pop()      
                i+=1

                start = i              
                while i<n and formula[i].isdigit():
                    i+=1
                multiplier = int(formula[start:i]) if formula[start:i] else 1

                for atom in curr_counter:
                    stack[-1][atom]+=curr_counter[atom]*multiplier
            else:
                atom = c
                i+=1

                start = i
                while i<n and formula[i].islower():
                    i+=1    
                atom+=formula[start:i]

                start = i
                while i<n and formula[i].isdigit():
                    i+=1
                count = int(formula[start:i]) if formula[start:i] else 1
                stack[-1][atom]+=count

        res = ""
        for key,value in sorted(stack[-1].items()):
            res+=key
            if value>1:
                res+=str(value)
        return res
        