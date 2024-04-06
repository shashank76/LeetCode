class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        out = []
        count = 0
        for i in s:
            if i == ")" and count < 1:
                next
            else:
                out.append(i)
                if i == "(":
                    count+=1
                elif i == ")":
                    count-=1
        res = []
        for i in out[::-1]:
            if i == '(' and count > 0:
                count-=1
            else:
                res.append(i)
        return "".join(res[::-1]) 
        